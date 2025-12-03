from pathlib import Path

# Базова директорія проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# !!! Можеш залишити свій ключ або цей тимчасовий (для навчання ок)
SECRET_KEY = 'django-insecure-elahog-5#+6hz8dtyfq@%(zkol83jjgr-0iti9oqw+27p)^87a'

# У продакшні став DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']



# ==========================
#   APPLICATIONS
# ==========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'barber',  # наш додаток перукарні
]


# ==========================
#   MIDDLEWARE
# ==========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================
#   URL / WSGI
# ==========================

ROOT_URLCONF = 'barber_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Якщо захочеш окрему папку templates на рівні проекту – можна додавати сюди
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'barber_site.wsgi.application'


# ==========================
#   DATABASE
# ==========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==========================
#   PASSWORD VALIDATION
# ==========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==========================
#   INTERNATIONALIZATION
# ==========================

LANGUAGE_CODE = 'uk'   # можна залишити 'en-us', якщо хочеш англійську

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_TZ = True


# ==========================
#   STATIC FILES (CSS/JS/IMG)
# ==========================
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'barber' / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")


# ==========================
#   DEFAULT AUTO FIELD
# ==========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [
        BASE_DIR / 'barber' / 'static',
    ]
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
