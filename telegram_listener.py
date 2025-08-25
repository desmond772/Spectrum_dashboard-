from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config
import logging

logging.basicConfig(level=logging.INFO)

client = TelegramClient(StringSession(config.TELETHON_SESSION), config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

@client.on(events.NewMessage(chats=[config.TELEGRAM_CHANNEL_ONE, config.TELEGRAM_CHANNEL_TWO]))
async def handler(event):
    try:
        # Your handler logic goes here
        logging.info(f"Received message from {event.chat_id}")
    except Exception as e:
        logging.error(f"Error handling message: {e}")

async def main():
    await client.start()
    logging.info("TelegramListener started. Waiting for messages...")
    await client.run_until_disconnected()
    logging.info("TelegramListener stopped.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
