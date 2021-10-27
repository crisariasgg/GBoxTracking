from .base import *

def show_toolbar(request):
    return True

# =================BASE=================
DEBUG = os.environ.get('DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

# =================SECURITY=================
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]


# =================TEMPLATES=================
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA


# =================CACHES=================
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION': '',
	}
}
# =================EMAIL=================
EMAIL_BACKEND = os.environ.get('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# =================APPS=================
INSTALLED_APPS += ['django_extensions','debug_toolbar']


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS':False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}