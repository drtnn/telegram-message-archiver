from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    TELETHON_API_ID: int
    TELETHON_API_HASH: str

    TELETHON_API_SESSION: str = "session"

    class Config:
        case_sensitive = True


telegram_settings = TelegramSettings()
