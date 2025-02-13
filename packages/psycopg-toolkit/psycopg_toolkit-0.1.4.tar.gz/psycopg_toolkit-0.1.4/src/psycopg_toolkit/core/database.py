import logging
from asyncio import Lock
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Callable, List, Optional, Awaitable

import psycopg
from psycopg_pool import AsyncConnectionPool
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import DatabaseSettings
from .transaction import TransactionManager
from ..exceptions import DatabaseConnectionError, DatabaseNotAvailable, DatabasePoolError

logger = logging.getLogger(__name__)


class Database:
    """
    Database management class that handles connection pooling and database operations.
    """

    def __init__(self, settings: DatabaseSettings):
        """
        Initialize Database instance with settings.

        Args:
            settings: Database connection settings

        Raises:
            ValueError: If settings are invalid
        """
        # Validate settings
        if not settings.host or not settings.dbname or not settings.user:
            raise ValueError("Invalid database settings: host, dbname, and user are required")

        self._pool: Optional[AsyncConnectionPool] = None
        self._settings = settings
        self._init_callbacks: List[Callable[[AsyncConnectionPool], Awaitable[None]]] = []
        self._transaction_manager: Optional[TransactionManager] = None
        self._pool_lock = Lock()
        self._callbacks_lock = Lock()
        self._transaction_manager_lock = Lock()

    async def get_transaction_manager(self) -> TransactionManager:
        """
        Get the transaction manager instance, creating it if necessary.

        Returns:
            TransactionManager: Instance for managing database transactions
        """
        if self._transaction_manager is None:
            async with self._transaction_manager_lock:
                if self._transaction_manager is None:
                    self._transaction_manager = TransactionManager(self)
        return self._transaction_manager

    async def register_init_callback(self, callback: Callable[[AsyncConnectionPool], Awaitable[None]]) -> None:
        """
        Register a callback to be executed after pool initialization.

        Args:
            callback: Async function that takes a pool instance and performs initialization
        """
        async with self._callbacks_lock:
            self._init_callbacks.append(callback)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def ping_postgres(self) -> bool:
        """
        Ping the PostgreSQL database to check if it's up and reachable.

        Returns:
            bool: True if connection successful

        Raises:
            DatabaseConnectionError: If connection fails
        """
        try:
            logger.info(f"Pinging PostgreSQL at host: {self._settings.host}, "
                        f"dbname: {self._settings.dbname}, "
                        f"user: {self._settings.user}")

            conn = psycopg.connect(
                self._settings.get_connection_string(self._settings.connection_timeout)
            )
            conn.close()
            logger.info("Successfully connected to PostgreSQL.")
            return True
        except Exception as e:
            error_msg = f"Could not connect to PostgreSQL"
            logger.error(f"Error: {error_msg}. Details: {e}")
            raise DatabaseConnectionError(error_msg) from e

    async def create_pool(self) -> AsyncConnectionPool:
        """
        Create a database connection pool if PostgreSQL is reachable.

        Returns:
            AsyncConnectionPool: Initialized connection pool

        Raises:
            DatabaseConnectionError: If database connection fails
            DatabasePoolError: If pool creation fails
        """
        try:
            if not self.ping_postgres():
                raise DatabaseConnectionError("Failed to ping database")

            logger.info("Initializing connection pool to PostgreSQL.")

            pool = AsyncConnectionPool(
                conninfo=self._settings.connection_string,
                min_size=self._settings.min_pool_size,
                max_size=self._settings.max_pool_size,
                timeout=self._settings.pool_timeout,
                open=False
            )

            try:
                await pool.open()
                self._pool = pool
            except Exception as e:
                await pool.close()
                raise DatabasePoolError("Failed to open pool") from e

            return pool
        except DatabaseConnectionError:
            raise
        except Exception as e:
            error_msg = "Could not create connection pool to PostgreSQL"
            logger.error(f"Error: {error_msg}. Details: {e}")
            raise DatabasePoolError(error_msg) from e

    async def get_pool(self) -> AsyncConnectionPool:
        """
        Get existing pool or create new one if none exists.

        Returns:
            AsyncConnectionPool: Database connection pool

        Raises:
            DatabaseNotAvailable: If database is not available
        """
        if not self._pool or self._pool.closed:
            async with self._pool_lock:
                if not self._pool or self._pool.closed:
                    try:
                        self._pool = await self.create_pool()
                    except Exception as e:
                        raise DatabaseNotAvailable("Database is not available") from e
        return self._pool

    @asynccontextmanager
    async def connection(self) -> AsyncGenerator[AsyncConnectionPool, None]:
        """
        Get a database connection from the pool.

        Yields:
            AsyncConnectionPool: Database connection from the pool

        Raises:
            DatabaseNotAvailable: If database is not available
        """
        pool = await self.get_pool()
        async with pool.connection() as conn:
            if self._settings.statement_timeout:
                await conn.execute(f"SET statement_timeout = {int(self._settings.statement_timeout * 1000)}")
            yield conn

    async def init_db(self) -> None:
        """
        Initialize the database pool and execute registered callbacks.

        Raises:
            DatabaseNotAvailable: If database is not available
            DatabaseConnectionError: If connection fails
            DatabasePoolError: If pool operations fail
        """
        try:
            pool = await self.get_pool()
            async with pool.connection() as _:
                logger.info("Database pool initialized successfully.")

                # Execute registered initialization callbacks with proper error handling
                async with self._callbacks_lock:
                    for callback in self._init_callbacks:
                        try:
                            await callback(pool)
                        except Exception as e:
                            logger.error(f"Callback failed: {e}")
                            await self.cleanup()
                            raise

        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            await self.cleanup()
            raise

    async def cleanup(self) -> None:
        """
        Cleanup database resources on shutdown.

        Raises:
            DatabasePoolError: If cleanup fails
        """
        async with self._pool_lock:
            if self._pool is not None:
                logger.info("Closing database connection pool...")
                try:
                    await self._pool.close()
                    logger.info("Database connection pool closed successfully.")
                except Exception as e:
                    logger.error(f"Error closing database pool: {e}")
                    raise DatabasePoolError("Failed to close database pool") from e
                finally:
                    self._pool = None
                    self._transaction_manager = None

    def is_pool_active(self) -> bool:
        """Check if pool exists and is not closed."""
        return self._pool is not None and not self._pool.closed

    async def check_pool_health(self) -> bool:
        """
        Perform a health check on the connection pool.

        Returns:
            bool: True if pool is healthy
        """
        try:
            pool = await self.get_pool()
            async with pool.connection() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT 1")
                    result = await cur.fetchone()
                    return result is not None and result[0] == 1
        except Exception as e:
            logger.error(f"Pool health check failed: {e}")
            return False
