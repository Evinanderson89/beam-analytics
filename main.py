from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from datetime import datetime
import logging

app = FastAPI()

@app.get("/track")
async def track(request: Request):
    params = dict(request.query_params)
    redirect_url = params.pop("redirect", "https://example.com")
    
    # Optional: log all query params
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent"),
        **params
    }
    logging.info(f"Tracked Click: {log_data}")

    return RedirectResponse(redirect_url)
