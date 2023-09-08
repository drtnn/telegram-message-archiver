import csv
import os
from datetime import datetime

from telethon.tl.patched import Message

from app.config.system import settings
from app.loader import client


def create_cache_dirs():
    if not os.path.exists(settings.CACHE_DIR):
        os.makedirs(settings.CACHE_DIR)

    if not os.path.exists(settings.CACHE_PER_DAY_DIR):
        os.makedirs(settings.CACHE_PER_DAY_DIR)


async def write_message(message: Message):
    if message.is_channel:
        return

    per_day_file = os.path.join(settings.CACHE_PER_DAY_DIR, datetime.now().strftime("%d-%m-%Y")) + ".csv"
    write_header = not os.path.isfile(per_day_file)

    from_id = getattr(message.from_id, "user_id", None)
    user = await client.get_entity(from_id) if from_id else None

    fieldnames = [
        "date", "chat_id", "first_name", "last_name", "username", "phone", "id", "message", "reply_to_msg_id",
        "forward_from_id", "type"
    ]
    with open(per_day_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow({
            "date": message.date.isoformat(),
            "chat_id": message.chat_id,
            "first_name": user.first_name if user else None,
            "last_name": user.last_name if user else None,
            "username": user.username if user else None,
            "phone": user.phone if user else None,
            "id": message.id,
            "message": message.message,
            "reply_to_msg_id": message.reply_to_msg_id,
            "forward_from_id": getattr(getattr(message.fwd_from, "from_id", None), "user_id", None),
            "type": None,
        })
