from telethon import TelegramClient, events
import config
import logging
from signal_parser import parse_signal_source_one, parse_signal_source_two

logging.basicConfig(level=logging.INFO)

class TelegramListener:
    def __init__(self, trade_executor):
        try:
            self.client = TelegramClient("session_name", config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
            self.trade_executor = trade_executor
            self.client.add_event_handler(self.handler, events.NewMessage(chats=[config.TELEGRAM_CHANNEL_ONE, config.TELEGRAM_CHANNEL_TWO]))
        except Exception as e:
            logging.error(f"Error initializing Telegram client: {e}")

    async def start(self):
        try:
            await self.client.start()
            await self.client.run_until_disconnected()
        except Exception as e:
            logging.error(f"Error starting Telegram client: {e}")

    async def handler(self, event):
        try:
            message = event.raw_text
            signal = parse_signal_source_one(message) or parse_signal_source_two(message)
            if signal:
                logging.info(f"Currency Pair: {signal['asset']}")
                logging.info(f"Entry Time: {signal['entry']}")
                logging.info(f"Direction: {signal['direction']}")
                logging.info(f"Martingale Levels: {signal['martingale_levels']}")
            else:
                logging.error("Message format not recognized")
        except Exception as e:
            logging.error(f"Error handling message: {e}")
