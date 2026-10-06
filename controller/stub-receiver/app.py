import logging
from datetime import datetime, timezone
from fastapi import FastAPI, Request

# Configure logging to stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("stub-receiver")

app = FastAPI(title="RTM Stub Receiver", description="Temporary webhook receiver for Falco alerts")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/alerts")
async def receive_alert(request: Request):
    payload = await request.json()
    now_iso = datetime.now(timezone.utc).isoformat()
    logger.info(f"[{now_iso}] FALCO ALERT RECEIVED:\n{payload}")
    return {"status": "ok", "received_at": now_iso}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
