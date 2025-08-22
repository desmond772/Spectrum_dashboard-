# Spectrum Dashboard

A professional trading dashboard and automation tool for Pocket Option, integrating with Telegram signals and supporting both demo and live accounts.

## Features

- Reads and parses signals from two Telegram channels
- Executes trades on Pocket Option via async API (demo/live switch)
- Implements Martingale strategy
- Generates performance reports and analytics
- Beautiful FastAPI dashboard (black & white)
- Robust error handling, monitoring, and keep-alive

## Setup

1. **Clone the repo:**  
   `git clone https://github.com/YOUR_USERNAME/spectrum-dashboard.git`

2. **Install dependencies:**  
   `pip install -r requirements.txt`

3. **Configure your `.env` file:**

   ```
   POCKET_OPTION_SSID_LIVE=your_live_ssid
   POCKET_OPTION_SSID_DEMO=your_demo_ssid
   TELEGRAM_API_ID=your_telegram_api_id
   TELEGRAM_API_HASH=your_telegram_api_hash
   TELEGRAM_CHANNEL_ONE=channel_one_id
   TELEGRAM_CHANNEL_TWO=channel_two_id
   DEFAULT_TRADE_AMOUNT=1.0
   TRADE_MODE=demo
   ```

4. **Run locally:**  
   `uvicorn main:app --reload`

5. **Deploy to Vercel:**  
   Push to GitHub, connect repo to Vercel, set environment variables.

## Structure

- `main.py`: Entrypoint
- `config.py`: Configuration
- `telegram_listener.py`: Telegram integration
- `signal_parser.py`: Signal parsing
- `trade_executor.py`: Trade logic
- `report_generator.py`: Analytics and reporting
- `dashboard/`: FastAPI app, templates, static assets

## Extend

- Add more signal sources, strategies, or UI features as needed!
