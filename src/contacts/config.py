from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CONTACTS_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "contacts"
    environment: str = "development"
    data_dir: Path = Field(default_factory=lambda: Path.home() / ".contacts")
    default_model: str = "unset"


settings = Settings()
