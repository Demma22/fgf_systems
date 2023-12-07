import os
from urllib.parse import quote
from pathlib import Path
import dj_database_url
from decouple import config
import dotenv
import environ

env = environ.Env()
environ.Env.read_env()
dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
SECRET_KEY = config("DJANGO_SECRET_KEY", default="default_secret_key")
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "animals",
    "plants",
    "cultures",
    "accounts",
    "django_filters",
    "corsheaders",
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "https://vercel.app",
    "http://localhost:5173",
    "http://localhost:8000",
    "https://render.com",
    "https://onrender.com",
    "https://3.75.158.163",
    "https://3.125.183.140",
    "https://35.157.117.28",
    "https://102.134.147.233",
]

CORS_ORIGIN_WHITELIST = ["http://localhost:5173"]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
MEDIA_URL = "images/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
    "VALIDATOR_URL": None,
    "PERSIST_AUTH": True,
}

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL").format(
            encoded_password=quote("befpc4iJOVEpaRNf_r9TpkkrZ##_8ep1")
        )
    )
}
