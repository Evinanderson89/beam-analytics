from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Beam Analytics is running! Use the /track endpoint with UTM parameters."}

@app.get("/track")
async def track(request: Request):
    params = dict(request.query_params)
    redirect_url = params.pop("redirect", "https://example.com")
    
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent"),
        **params
    }
    logging.info(f"Tracked Click: {log_data}")

    return RedirectResponse(redirect_url)
