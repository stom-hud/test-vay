# Test Time Backend (FastAPI)

Простой тестовый бэкенд на FastAPI, который возвращает текущее время сервера.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload
```

## Проверка

- Health-check: `http://127.0.0.1:8000/health`
- Endpoint времени: `http://127.0.0.1:8000/time`
- Endpoint даты: `http://127.0.0.1:8000/date`
- Endpoint даты и времени: `http://127.0.0.1:8000/date-time`
- Swagger UI: `http://127.0.0.1:8000/docs`

Пример ответа `GET /time`:

```json
{
  "server_time_utc": "2026-05-07T11:35:00.000000+00:00",
  "unix_timestamp": 1778153700.0
}
```
