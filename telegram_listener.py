from telethon import TelegramClient, events
import config
import re

class TelegramListener:
    def __init__(self):
        self.client = TelegramClient("session_name", config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
        self.client.add_event_handler(self.handler, events.NewMessage(chats=[config.TELEGRAM_CHANNEL_ONE, config.TELEGRAM_CHANNEL_TWO]))

    async def start(self):
        await self.client.start()
        await self.client.run_until_disconnected()

    async def handler(self, event):
        message = event.raw_text

        # Source One message pattern
        pattern_one = re.compile(r"([A-Z]{3}/[A-Z]{3}).*?Expiration \d+M.*?Entry at (\d{2}:\d{2}).*?(BUY|PUT).*?Martingale levels.*?1️⃣ level at (\d{2}:\d{2}).*?2️⃣ level at (\d{2}:\d{2}).*?3️⃣ level at (\d{2}:\d{2})", re.DOTALL)

        # Source Two message pattern
        pattern_two = re.compile(r"\d+ minutes expiry ([A-Z]{3}/[A-Z]{3});(\d{2}:\d{2});(PUT|CALL|BUY).*?TIME TO (\d{2}:\d{2}) — TIME TO (\d{2}:\d{2})", re.DOTALL)

        match_one = pattern_one.search(message)
        match_two = pattern_two.search(message)

        if match_one:
            # Extract information from match_one
            currency_pair = match_one.group(1)
            entry_time = match_one.group(2)
            direction = match_one.group(3)
            martingale_level_1 = match_one.group(4)
            martingale_level_2 = match_one.group(5)
            martingale_level_3 = match_one.group(6)

            log_info(f"Currency Pair: {currency_pair}")
            log_info(f"Entry Time: {entry_time}")
            log_info(f"Direction: {direction}")
            log_info(f"Martingale Levels: {martingale_level_1}, {martingale_level_2}, {martingale_level_3}")
        elif match_two:
            # Extract information from match_two
            currency_pair = match_two.group(1)
            entry_time = match_two.group(2)
            direction = match_two.group(3)
            martingale_level_1 = match_two.group(4)
            martingale_level_2 = match_two.group(5)

            log_info(f"Currency Pair: {currency_pair}")
            log_info(f"Entry Time: {entry_time}")
            log_info(f"Direction: {direction}")
            log_info(f"Martingale Levels: {martingale_level_1}, {martingale_level_2}")
        else:
            log_error("Message format not recognized")
