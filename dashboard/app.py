from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import config
from report_generator import ReportGenerator

app = FastAPI()
app.mount("/static", StaticFiles(directory="dashboard/static"), name="static")
templates = Jinja2Templates(directory="dashboard/templates")

trade_mode = config.TRADE_MODE
report = ReportGenerator()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    # Dummy account balances for demo purposes
    demo_balance = 1000
    live_balance = 500
    summary = report.summary()
    data = {
        "mode": trade_mode,
        "demo_balance": demo_balance,
        "live_balance": live_balance,
        "source_one": summary["sources"].get("one", {"wins": 0, "losses": 0, "martingale_wins": 0, "status": "stopped", "martingale_level": "-"}),
        "source_two": summary["sources"].get("two", {"wins": 0, "losses": 0, "martingale_wins": 0, "status": "stopped", "martingale_level": "-"}),
        "combined": summary["combined"],
    }
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})

@app.post("/switch-mode")
async def switch_mode(request: Request, mode: str = Form(...)):
    global trade_mode
    trade_mode = mode
    return RedirectResponse("/", status_code=303)

def create_dashboard_app():
    return app
