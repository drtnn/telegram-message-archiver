from telethon import TelegramClient

from app.config.telegram import telegram_settings

client = TelegramClient(
    telegram_settings.TELETHON_API_SESSION,
    telegram_settings.TELETHON_API_ID,
    telegram_settings.TELETHON_API_HASH
)