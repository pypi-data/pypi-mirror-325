from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Chatwoot
    frontend_url: str = ""

    # Postgres
    postgres_database: str = ""
    postgres_username: str = ""
    postgres_password: str = ""
    postgres_host: str = ""
    postgres_port: str = ""

    # General
    log_level: str = ""

settings = Settings()
