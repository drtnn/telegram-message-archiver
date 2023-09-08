from telethon import events
from telethon.events.newmessage import NewMessage

from app.loader import client
from app.utils import create_cache_dirs, write_message


@client.on(events.NewMessage(incoming=True))
async def all_messages_handler(event: NewMessage.Event):
    await write_message(event.message)


if __name__ == "__main__":
    create_cache_dirs()
    client.start()
    client.run_until_disconnected()
