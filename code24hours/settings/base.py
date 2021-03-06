"""
Django settings for code24hours project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

def env_or_default(NAME, default):
    return os.environ.get(NAME, default)

# Top level of our source / repository
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY')


# Quick-start development settings - unsuitable for production

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'code24hours.urls'

WSGI_APPLICATION = 'code24hours.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env_or_default("DB_NAME", "code24hours"),
        "USER": env_or_default("DB_USER", ""),
        "PASSWORD": env_or_default("DB_PASSWORD", ""),
        "HOST": env_or_default("DB_HOST", ""),
        "PORT": env_or_default("DB_PORT", ""),
    }
}

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates"),
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "US/Pacific"

USE_I18N = True

USE_L10N = True

USE_TZ = True


