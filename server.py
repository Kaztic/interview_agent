from fastapi import FastAPI
from api.endpoints import router as api_router
from core.config import get_settings

app = FastAPI(title="Interview Agent API")
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "healthy", "version": get_settings().APP_VERSION}