"""
Main config for backend service
"""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class PostgresSettings(BaseSettings):
    """
    Base settings Pydantic class with postgres connection params
    """
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str

    @property
    def database_url(self) -> str:
        """ Function that creates postgres connection url
        :return: string connection url
        """
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    model_config = {
        "env_file": ".env",
        "from_attributes": True,
        'extra': 'ignore'
    }


class AppSettings(BaseSettings):
    """
    Base settings Pydantic class with app params
    """
    secret_key: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    algorithm: str

    model_config = {
        "env_file": ".env",
        "from_attributes": True,
        'extra': 'ignore',
    }


postgres_settings = PostgresSettings()

app_settings = AppSettings()
