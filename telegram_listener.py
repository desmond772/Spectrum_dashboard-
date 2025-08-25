from telethon import TelegramClient, events
import config
import logging
from signal_parser import parse_signal_source_one, parse_signal_source_two
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO)

class TelegramListener:
    def __init__(self, trade_executor):
        """ 
        Initializes the TelegramListener with a trade executor.
        
        Args:
            trade_executor: The trade executor to use.
        """
        try:
            self.client = TelegramClient(StringSession(config.TELETHON_SESSION), int(config.TELEGRAM_API_ID), config.TELEGRAM_API_HASH)
            self.trade_executor = trade_executor
            self.client.add_event_handler(self.handler, events.NewMessage(chats=[int(config.TELEGRAM_CHANNEL_ONE), int(config.TELEGRAM_CHANNEL_TWO)]))
            logging.info("TelegramListener initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing Telegram client: {e}")

    async def start(self) -> None:
        """ 
        Starts the TelegramListener.
        """
        try:
            await self.client.start()
            logging.info("Telegram connected successfully")
            logging.info("TelegramListener started successfully")
            await self.client.run_until_disconnected()
        except Exception as e:
            logging.error(f"Error starting Telegram client: {e}")
        finally:
            await self.client.disconnect()

    async def handler(self, event: events.NewMessage.Event):
        # Your handler logic goes here
        pass
