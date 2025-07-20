import os
from pydantic import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "A FastAPI template for building APIs."
    PROJECT_URL: str = ""
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DB_USER: str = "fastapi_user"
    DB_PASSWORD: str = "fastapi_pass"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "fastapi_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    S3_BUCKET_NAME: str = "my-s3-bucket"
    EMAIL_HOST: str = "smtp.mailtrap.io"
    EMAIL_PORT: int = 587
    EMAIL_USER: str = "user"
    EMAIL_PASSWORD: str = "password"

class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"

settings = Settings()