from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_URL: str
    GEMINI_API_KEY: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    APP_VERSION: str = "0.1.0"
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()