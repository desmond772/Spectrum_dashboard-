import re
from datetime import datetime, timedelta

def parse_signal_source_one(text):
    # Example: 🇬🇧 GBP/JPY 🇯🇵 OTC 🕘 Expiration 5M ⏺ Entry at 04:25 🟩 BUY 🔼 Martingale levels 1️⃣ level at 04:30 2️⃣ level at 04:35 3️⃣ level at 04:40
    pattern = re.compile(r"([A-Z]{3}/[A-Z]{3}).*?Expiration (\d+)M.*?Entry at (\d{2}:\d{2}).*?(BUY|PUT).*?Martingale levels.*?1️⃣ level at (\d{2}:\d{2}).*?2️⃣ level at (\d{2}:\d{2}).*?3️⃣ level at (\d{2}:\d{2})", re.DOTALL)
    m = pattern.search(text)
    if m:
        asset, duration, entry, direction, level1, level2, level3 = m.groups()
        return {
            "asset": asset.replace("/", "_").upper() + "_otc",
            "duration": int(duration) * 60,
            "entry": entry,
            "direction": direction,
            "martingale_levels": [level1, level2, level3],
            "raw": text,
        }
    return None

def parse_signal_source_two(text):
    # Example: ⏰ Time Zone: UTC -3 💰5 minutes expiry USD/COP;00:10;PUT 🕐TIME TO 00:15 1ST GALE — TIME TO 00:20 2ND GALE
    pattern = re.compile(r"expiry ([A-Z]{3}/[A-Z]{3});(\d{2}:\d{2});(PUT|CALL|BUY).*?TIME TO (\d{2}:\d{2}) 1ST GALE.*?TIME TO (\d{2}:\d{2}) 2ND GALE", re.DOTALL)
    m = pattern.search(text)
    if m:
        asset, entry, direction, level1, level2 = m.groups()
        # Convert UTC-3 time to UTC-4
        def convert_time(t):
            dt = datetime.strptime(t, "%H:%M") - timedelta(hours=1)
            return dt.strftime("%H:%M")
        entry = convert_time(entry)
        level1 = convert_time(level1)
        level2 = convert_time(level2)
        return {
            "asset": asset.replace("/", "_").upper() + "_otc",
            "duration": 300,
            "entry": entry,
            "direction": direction,
            "martingale_levels": [level1, level2],
            "raw": text,
        }
    return None
