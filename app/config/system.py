import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    CACHE_DIR: str = os.path.join(APP_DIR, "cache")
    CACHE_PER_DAY_DIR: str = os.path.join(CACHE_DIR, "per_day")

    class Config:
        case_sensitive = True


settings = Settings()
