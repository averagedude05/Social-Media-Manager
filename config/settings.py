import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"

INSTALLED_APPS = [
    # ... default apps ...
    "corsheaders",
    "accounts",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # must be first
    # ... default middleware ...
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

