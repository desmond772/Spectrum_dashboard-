import os
from dotenv import load_dotenv

load_dotenv()

POCKET_OPTION_SSID_LIVE = os.getenv("POCKET_OPTION_SSID_LIVE", "")
POCKET_OPTION_SSID_DEMO = os.getenv("POCKET_OPTION_SSID_DEMO", "")
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID", "")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "")
TELEGRAM_CHANNEL_ONE = os.getenv("TELEGRAM_CHANNEL_ONE", "")
TELEGRAM_CHANNEL_TWO = os.getenv("TELEGRAM_CHANNEL_TWO", "")
DEFAULT_TRADE_AMOUNT = float(os.getenv("DEFAULT_TRADE_AMOUNT", "1.0"))
TRADE_MODE = os.getenv("TRADE_MODE", "demo")  # "demo" or "live"
REPORT_PERIODS = ["daily", "weekly", "monthly", "all"]
