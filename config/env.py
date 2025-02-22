from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=str,
    ALLOWED_HOSTS=list,
    CORS_ALLOWED_ORIGINS=(list, list()),
    CSRF_TRUSTED_ORIGINS=(list, list()),
    # Database
    POSTGRES_DB=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    POSTGRES_HOST=str,
    POSTGRES_PORT=int,
    # Redis
    REDIS_HOST=str,
    REDIS_PORT=int,
    # S3
    AWS_S3_ACCESS_KEY_ID=str,
    AWS_S3_SECRET_ACCESS_KEY=str,
    AWS_STORAGE_BUCKET_NAME=str,
    AWS_S3_REGION_NAME=str,
)
