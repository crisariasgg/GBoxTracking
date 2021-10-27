from .base import *
import dj_database_url
from decouple import config

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG')


ALLOWED_HOSTS = ['gboxtracking-test.herokuapp.com']


MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


# Gunicorn
INSTALLED_APPS += ['gunicorn']  # noqa F405


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


DATABASES = {
    "default": {
        dj_database_url.config(default=config('DATABASE_URL'))
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
