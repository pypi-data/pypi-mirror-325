from contextlib import contextmanager, asynccontextmanager
from sqlalchemy import create_engine, event, Pool, text, NullPool
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import DatabaseConfig


class DatabaseInstance:

    def __init__(self, config: DatabaseConfig):
        self.db_user = config.get('db_user')
        self.db_password = config.get('db_password')
        self.db_host = config.get('db_host')
        self.db_port = config.get('db_port')
        self.db_name = config.get('db_name')
        self.db_ssl = config.get('db_ssl', False)
        self.db_pool_size = config.get('db_pool_size', None)
        self.db_max_overflow = config.get('db_max_overflow', 0)

        self.active_connections = 0

        # Build database connection URLs
        self.database_path = self._build_database_url(async_mode=False)
        self.async_database_path = self._build_database_url(async_mode=True)

        # Database settings
        db_settings = self._initialize_db_settings()

        # Create synchronous and asynchronous engines and sessions
        self.engine = create_engine(self.database_path, **db_settings)
        self.scoped_session = scoped_session(sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=True
        ))

        self.async_engine = create_async_engine(self.async_database_path, **db_settings)
        self.async_session_maker = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=True, class_=AsyncSession,
            autocommit=False, autoflush=False
        )

        # Declarative base for ORM models
        self.base = declarative_base(name="Base")

    def _build_database_url(self, async_mode=False):
        scheme = "postgresql+asyncpg" if async_mode else "postgresql"
        url = f"{scheme}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

        if self.db_ssl:
            url += "?ssl=require" if async_mode else "?sslmode=require"
        return url

    def _initialize_db_settings(self):
        db_settings = {"pool_pre_ping": True, "echo": False}

        if self.db_pool_size:
            db_settings.update({
                "pool_size": self.db_pool_size,
                "pool_recycle": 300,
                "pool_use_lifo": True,
                "max_overflow": self.db_max_overflow,
            })
        else:
            db_settings["poolclass"] = NullPool

        return db_settings

    def session_local(self):
        return self.scoped_session()

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    @contextmanager
    def get_db_cm(self):
        db = self.session_local()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def get_clean_db(self):
        db = self.session_local()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.expunge_all()
            db.close()

    @contextmanager
    def get_clean_db_cm(self):
        db = self.session_local()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.expunge_all()
            db.close()

    def create_tables(self):
        self.base.metadata.create_all(self.engine)

    def close_all_connections(self):
        self.engine.dispose()
        print("All connections closed gracefully.")

    def setup_connection_monitoring(self):
        @event.listens_for(Pool, "connect")
        def connect_listener(dbapi_connection, connection_record):
            self.active_connections += 1
            print(f"New database connection created. Total active connections: {self.active_connections}")

        @event.listens_for(Pool, "close")
        def close_listener(dbapi_connection, connection_record):
            self.active_connections -= 1
            print(f"A database connection closed. Total active connections: {self.active_connections}")

    def check_database_health(self):
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Database health check failed: {e}")
            return False

    def async_session_local(self):
        return self.async_session_maker()

    async def async_get_db(self):
        db = self.async_session_local()
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        finally:
            await db.close()

    async def async_get_clean_db(self):
        db = self.async_session_local()
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        finally:
            db.expunge_all()
            await db.close()

    @asynccontextmanager
    async def async_get_db_cm(self):
        db = self.async_session_local()
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        finally:
            await db.close()

    @asynccontextmanager
    async def async_get_clean_db_cm(self):
        db = self.async_session_local()
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        finally:
            db.expunge_all()
            await db.close()
