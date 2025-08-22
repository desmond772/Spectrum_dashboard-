import os
from dotenv import load_dotenv

load_dotenv()

POCKET_OPTION_SSID_LIVE = os.getenv("POCKET_OPTION_SSID_LIVE", "")
POCKET_OPTION_SSID_DEMO = os.getenv("POCKET_OPTION_SSID_DEMO", "")
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID"29630724")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH"8e12421a95fd722246e0c0b194fd3e0c")
TELEGRAM_CHANNEL_ONE = os.getenv("TELEGRAM_CHANNEL_ONE"-1002074799242")
TELEGRAM_CHANNEL_TWO = os.getenv("TELEGRAM_CHANNEL_TWO"-1001940077808")
DEFAULT_TRADE_AMOUNT = float(os.getenv("DEFAULT_TRADE_AMOUNT", "1.0"))
TRADE_MODE = os.getenv("TRADE_MODE", "demo")  # "demo" or "live"
REPORT_PERIODS = ["daily", "weekly", "monthly", "all"]
