import sys
import os
from logging.config import fileConfig
from sqlalchemy import create_engine, text
from alembic import context

from src.models.base import Base
from src.models.catalog import Agency, Profession, Ethnicity, Gender
from dotenv import load_dotenv

load_dotenv()
schema = "test"
config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"},
        include_schemas=True, version_table_schema=schema
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = os.getenv("DATABASE_URL")
    connectable = create_engine(url)

    with connectable.connect() as connection:
        # connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
        context.configure(connection=connection, target_metadata=target_metadata,
            include_schemas=True, version_table_schema=schema)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()