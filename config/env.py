from pathlib import Path

import environ

environ.Env.read_env()


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
    # Middleware
    MIDDLEWARE_BASE_URL=str,
)


BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")
