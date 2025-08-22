import asyncio
from pocketoptionapi_async import AsyncPocketOptionClient, OrderDirection
import config
from report_generator import ReportGenerator

class TradeExecutor:
    def __init__(self):
        self.mode = config.TRADE_MODE
        self.client = AsyncPocketOptionClient(
            ssid=config.POCKET_OPTION_SSID_DEMO if self.mode == "demo" else config.POCKET_OPTION_SSID_LIVE,
            is_demo=(self.mode == "demo"),
            persistent_connection=True,
        )
        self.report = ReportGenerator()
        self.running = True

    async def run(self):
        await self.client.connect()
        while self.running:
            await asyncio.sleep(1)

    async def handle_signal(self, signal, source):
        # Payout check for Source Two
        if source == "two":
            payout = await self.get_asset_payout(signal["asset"])
            if payout < 80:
                return
        # Martingale execution
        entry_times = [signal["entry"]] + signal.get("martingale_levels", [])
        for level, entry_time in enumerate(entry_times):
            now = self.get_current_time()
            if now >= entry_time:
                result = await self.place_trade(
                    signal["asset"], config.DEFAULT_TRADE_AMOUNT, signal["direction"], signal["duration"]
                )
                self.report.log_trade(result, source, level)
                if result.status == "win":
                    break

    async def get_asset_payout(self, asset):
        # Fetch payout info (requires proper event handling in client)
        # For demo, return 90
        return 90

    async def place_trade(self, asset, amount, direction, duration):
        dir_map = {"BUY": OrderDirection.CALL, "CALL": OrderDirection.CALL, "PUT": OrderDirection.PUT}
        return await self.client.place_order(asset, amount, dir_map.get(direction, OrderDirection.CALL), duration)

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M")
