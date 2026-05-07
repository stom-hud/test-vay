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


@app.get("/date-time")
def get_date_time() -> dict[str, str]:
    now = datetime.now(timezone.utc)
    return {
        "date_utc": now.strftime("%Y-%m-%d"),
        "time_utc": now.strftime("%H:%M:%S"),
        "datetime_utc": now.isoformat(),
    }


@app.get("/date")
def get_current_date() -> dict[str, str]:
    now = datetime.now(timezone.utc)
    return {"date_utc": now.strftime("%Y-%m-%d")}
