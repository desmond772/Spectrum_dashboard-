from telethon import TelegramClient, events
import config
import logging
from signal_parser import parse_signal_source_one, parse_signal_source_two
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO)

class TelegramListener:
    def __init__(self, trade_executor):
        """ Initializes the TelegramListener with a trade executor.
        
        Args:
            trade_executor: The trade executor to use.
        """
        try:
            self.client = TelegramClient(StringSession(config.TELETHON_SESSION), int(config.TELEGRAM_API_ID), config.TELEGRAM_API_HASH)
            self.trade_executor = trade_executor
            self.client.add_event_handler(self.handler, events.NewMessage(chats=[config.TELEGRAM_CHANNEL_ONE, config.TELEGRAM_CHANNEL_TWO]))
            logging.info("TelegramListener initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing Telegram client: {e}")

    async def start(self) -> None:
        """ Starts the TelegramListener.
        """
        try:
            await self.client.start()
            logging.info("TelegramListener started successfully")
            await self.client.run_until_disconnected()
        except Exception as e:
            logging.error(f"Error starting Telegram client: {e}")
        finally:
            await self.client.disconnect()

    async def handler(self, event: events.NewMessage.Event) -> None:
        """ Handles a new message event.
        
        Args:
            event: The new message event.
        """
        try:
            if event is None:
                logging.error("Received None event")
                return
            logging.info(f"Received new message: {event.raw_text}")
            message = event.raw_text
            try:
                signal = parse_signal_source_one(message) or parse_signal_source_two(message)
            except Exception as e:
                logging.error(f"Error parsing signal: {e}")
                return
            if signal:
                logging.info(f"Currency Pair: {signal['asset']}")
                logging.info(f"Entry Time: {signal['entry']}")
                logging.info(f"Direction: {signal['direction']}")
                logging.info(f"Martingale Levels: {signal['martingale_levels']}")
            else:
                logging.error("Message format not recognized")
        except Exception as e:
            logging.error(f"Error handling message: {e}")

if __name__ == "__main__":
    pass
