import asyncio
from dashboard.app import create_dashboard_app
from trade_executor import TradeExecutor
from telegram_listener import TelegramListener
import config
import logging
from fastapi import APIRouter, BackgroundTasks

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = create_dashboard_app()
router = APIRouter()
trade_executor = TradeExecutor()
telegram_listener = TelegramListener(trade_executor)
running = False
task = None

async def run():
    try:
        logging.info("Starting application...")
        await asyncio.gather(
            telegram_listener.start(),
            trade_executor.run(),
        )
        logging.info("Application started successfully")
    except asyncio.CancelledError:
        logging.info("Application cancelled")
    except Exception as e:
        logging.error(f"Error running application: {e}", exc_info=True)
    finally:
        global running
        running = False
        logging.info("Application stopped")

@router.post("/start")
async def start():
    global running, task
    if not running:
        running = True
        task = asyncio.create_task(run())
        return {"message": "Bot started successfully"}
    else:
        return {"message": "Bot is already running"}

@router.post("/stop")
async def stop():
    global running, task
    if running:
        running = False
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        return {"message": "Bot stopped successfully"}
    else:
        return {"message": "Bot is already stopped"}

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    try:
        logging.info("Startup event triggered")
    except Exception as e:
        logging.error(f"Error in startup event: {e}", exc_info=True)

@app.on_event("shutdown")
async def shutdown_event():
    try:
        logging.info("Shutdown event triggered")
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
    except Exception as e:
        logging.error(f"Error in shutdown event: {e}", exc_info=True)
