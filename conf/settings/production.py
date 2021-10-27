from .base import *

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
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env('DATABASE_NAME'),
        "USER": env('DATABASE_USER'),
        "PASSWORD": env('DATABASE_PASSWORD'),
        "HOST": ('DATABASE_HOST'),
        "PORT": env('DATABASE_PORT'),
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
