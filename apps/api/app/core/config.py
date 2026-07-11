from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """
    Application configuration.
    """

    app_name: str = "Customer360 API"
    app_version: str = "0.4.0"
    debug: bool = True

    database_url: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
    )


settings = Settings()
