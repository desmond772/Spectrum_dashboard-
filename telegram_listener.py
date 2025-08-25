from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

class TelegramListener:
    def __init__(self, trade_executor=None):
        self.client = TelegramClient(StringSession(config.TELETHON_SESSION), int(config.TELEGRAM_API_ID), config.TELEGRAM_API_HASH)
        self.trade_executor = trade_executor

    async def start(self):
        await self.client.start()
        self.client.add_event_handler(self.handler, events.NewMessage(chats=[int(config.TELEGRAM_CHANNEL_ONE), int(config.TELEGRAM_CHANNEL_TWO)]))
        logging.info("TelegramListener started. Waiting for messages...")
        await self.client.run_until_disconnected()
        logging.info("TelegramListener stopped.")

    async def handler(self, event):
        try:
            # Your handler logic goes here
            logging.info(f"Received message from {event.chat_id}")
        except Exception as e:
            logging.error(f"Error handling message: {e}")

if __name__ == "__main__":
    listener = TelegramListener()
    asyncio.run(listener.start())
