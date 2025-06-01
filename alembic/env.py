from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import sys
import os
from services.db import Base

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migration_offline():
    """Run migrations in 'offline' mode.
    
    This configures the context with just a URL
    and not an engine, though an engine is acceptable
    here as well. By skipping the engine creation
    we don't even need a DBAPI to be available.
    
    Calls to context.execute() here emit the given string to the
    script output.
    
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    
    In this scenario we need to create an engine
    and associate a connection with the context.
    
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section,),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migration_offline()
else:
    run_migrations_online()
    