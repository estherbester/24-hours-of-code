from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = "--fake secret key for dev only--"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env_or_default("DB_NAME", "code24hours"),
        "USER": env_or_default("DB_USER", "rsanders"),
        "PASSWORD": env_or_default("DB_PASSWORD", ""),
        "HOST": env_or_default("DB_HOST", "localhost"),
        "PORT": env_or_default("DB_PORT", "5432"),
    }
}