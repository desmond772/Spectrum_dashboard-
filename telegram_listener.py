from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

class TelegramListener:
    def __init__(self):
        self.client = TelegramClient(StringSession(config.TELETHON_SESSION), int(config.TELEGRAM_API_ID), config.TELEGRAM_API_HASH)

    @self.client.on(events.NewMessage(chats=[int(config.TELEGRAM_CHANNEL_ONE), int(config.TELEGRAM_CHANNEL_TWO)]))
    async def handler(self, event):
        try:
            # Your handler logic goes here
            logging.info(f"Received message from {event.chat_id}")
        except Exception as e:
            logging.error(f"Error handling message: {e}")

    async def start(self):
        await self.client.start()
        logging.info("TelegramListener started. Waiting for messages...")
        await self.client.run_until_disconnected()
        logging.info("TelegramListener stopped.")

# Usage
if __name__ == "__main__":
    listener = TelegramListener()
    asyncio.run(listener.start())
