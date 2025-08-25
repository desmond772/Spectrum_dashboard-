import asyncio
from dashboard.app import include_dashboard_app
from trade_executor import TradeExecutor
from telegram_listener import TelegramListener
import config
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logging.info("Startup event triggered")
    except Exception as e:
        logging.error(f"Error in startup event: {e}", exc_info=True)
    yield
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

app = FastAPI(lifespan=lifespan)

@app.post("/start")
async def start():
    global running, task
    if not running:
        running = True
        task = asyncio.create_task(run())
        return {"message": "Bot started successfully"}
    else:
        return {"message": "Bot is already running"}

@app.post("/stop")
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

try:
    include_dashboard_app(app)
except Exception as e:
    logging.error(f"Error including dashboard app: {e}", exc_info=True)
