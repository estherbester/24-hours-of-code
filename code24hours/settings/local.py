from .base import *

SECRET_KEY = 'a^a-1#5=h_4p9f9*75yu$-q3y(7s!onf2$ra-qo9^_*3@*a2qx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


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