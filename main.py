import asyncio
from dashboard.app import create_dashboard_app
from trade_executor import TradeExecutor
from telegram_listener import TelegramListener
import config

app = create_dashboard_app()

# Entrypoint for bot and dashboard
if __name__ == "__main__":
    async def run():
        # Start trading executor and telegram listener
        trade_executor = TradeExecutor()
        telegram_listener = TelegramListener(trade_executor)
        await asyncio.gather(
            telegram_listener.start(),
            trade_executor.run(),
        )

    # Run FastAPI app for dashboard (for Vercel, entrypoint is app)
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
