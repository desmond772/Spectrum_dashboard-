import asyncio
from dashboard.app import create_dashboard_app
from trade_executor import TradeExecutor
from telegram_listener import TelegramListener
import config

app = create_dashboard_app()

async def run():
    trade_executor = TradeExecutor()
    telegram_listener = TelegramListener(trade_executor)
    await asyncio.gather(
        telegram_listener.start(),
        trade_executor.run(),
    )

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run())
