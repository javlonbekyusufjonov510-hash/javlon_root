
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="JAVLON ROOT")

@app.get("/")
def home():
    return {
        "robot": "JAVLON ROOT",
        "status": "ONLINE",
        "account": "DEMO",
        "symbol": "GOLD",
        "time": datetime.utcnow().isoformat()
    }

@app.get("/status")
def status():
    return {
        "robot": "JAVLON ROOT",
        "status": "READY",
        "trading": False,
        "message": "Demo server tayyor. Real savdo ulanmagan."
    }
