from collections import defaultdict
import config

class ReportGenerator:
    def __init__(self):
        self.trades = []
        self.stats = defaultdict(lambda: {"wins": 0, "losses": 0, "martingale_wins": 0})

    def log_trade(self, result, source, martingale_level):
        trade = {
            "source": source,
            "result": result.status,
            "martingale_level": martingale_level,
        }
        self.trades.append(trade)
        if result.status == "win":
            self.stats[source]["wins"] += 1
            if martingale_level > 0:
                self.stats[source]["martingale_wins"] += 1
        else:
            self.stats[source]["losses"] += 1

    def summary(self, period="all"):
        # For demo, returns all-time stats
        combined = {"wins": 0, "losses": 0, "martingale_wins": 0}
        for src, stat in self.stats.items():
            combined["wins"] += stat["wins"]
            combined["losses"] += stat["losses"]
            combined["martingale_wins"] += stat["martingale_wins"]
        return {"sources": dict(self.stats), "combined": combined}
