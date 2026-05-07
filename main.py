from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Test Time Backend")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/time")
def get_server_time() -> dict[str, float | str]:
    now = datetime.now(timezone.utc)
    return {
        "server_time_utc": now.isoformat(),
        "unix_timestamp": now.timestamp(),
    }
