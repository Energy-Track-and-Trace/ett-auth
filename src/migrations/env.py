import os
import sys
from logging.config import fileConfig
from alembic import context

from auth_api.models import *   # noqa: F403

sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.split(
                os.path.abspath(__file__))[0]), '..')
)


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)


def run_migrations():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    with db.engine.connect() as connection:     # noqa: F405
        context.configure(
            connection=connection,
            target_metadata=db.registry.metadata,   # noqa: F405
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations()
