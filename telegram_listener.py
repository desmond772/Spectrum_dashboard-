from telethon import TelegramClient, events
import config
from signal_parser import parse_signal_source_one, parse_signal_source_two

class TelegramListener:
    def __init__(self, trade_executor):
        self.client = TelegramClient("session", config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
        self.trade_executor = trade_executor

    async def start(self):
        await self.client.start()
        
        @self.client.on(events.NewMessage(chats=int(config.TELEGRAM_CHANNEL_ONE)))
        async def handler_one(event):
            print("Received message from Channel One:")
            print(event.raw_text)
            signal = parse_signal_source_one(event.raw_text)
            print("Parsed signal:", signal)
            if signal:
                await self.trade_executor.handle_signal(signal, source="one")

        @self.client.on(events.NewMessage(chats=int(config.TELEGRAM_CHANNEL_TWO)))
        async def handler_two(event):
            print("Received message from Channel Two:")
            print(event.raw_text)
            signal = parse_signal_source_two(event.raw_text)
            print("Parsed signal:", signal)
            if signal:
                await self.trade_executor.handle_signal(signal, source="two")
        
        await self.client.run_until_disconnected()
