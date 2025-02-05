from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Chatwoot
    chatwoot_base_url: str = ""

    # Postgres
    db_name: str = ""
    db_user: str = ""
    db_password: str = ""
    db_host: str = ""
    db_port: str = ""

    # General
    log_level: str = ""


settings = Settings()
