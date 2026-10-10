from fastapi import FastAPI

from app.config import APP_NAME, DEBUG, HOST, PORT

app = FastAPI(title=APP_NAME, debug=DEBUG)


@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "ok", "app": APP_NAME}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=DEBUG)
