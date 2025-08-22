import os
from dotenv import load_dotenv

load_dotenv()

POCKET_OPTION_SSID_LIVE = '42["auth",{"session":"R1yh0xAHwNZLSOagoOYKwHhgbVEQbArHjl1FGAqzQPsuJTj_FJ0ijXziAZYKF1Ez34U_zA","isDemo":0}]'
POCKET_OPTION_SSID_DEMO = '42["auth",{"session":"R1yh0xAHwNZLSOagoOYKwHhgbVEQbArHjl1FGAqzQPsuJTj_FJ0ijXziAZYKF1Ez34U_zA","isDemo":1}]'
TELEGRAM_API_ID = "29630724"
TELEGRAM_API_HASH = "8e12421a95fd722246e0c0b194fd3e0c"
TELEGRAM_CHANNEL_ONE = "-1002838415996"
TELEGRAM_CHANNEL_TWO = "-1001940077808"
DEFAULT_TRADE_AMOUNT = 1.0
TRADE_MODE = "demo"  # "demo" or "live"
REPORT_PERIODS = ["daily", "weekly", "monthly", "all"]
