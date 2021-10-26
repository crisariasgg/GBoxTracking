"""
WSGI config for project.
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.development')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)


