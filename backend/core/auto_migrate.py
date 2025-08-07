from alembic import command
from alembic.config import Config
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_migrations():
    try:
        logger.info("Starting database migrations")
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        logger.info("Database migrations completed")
    except Exception as e:
        logger.error(f"Error during migrations: {str(e)}")
        raise


if __name__ == "__main__":
    run_migrations()
