"""
This is the settings file used in production.
First, it imports all default settings, then overrides respective ones.
Secrets are stored in and imported from an additional file, not set under version control.
"""

from d120.settings import *
import d120.settings_secrets as secrets

SECRET_KEY = secrets.SECRET_KEY

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'djangocms',
        'USER': 'djangocms',
        'PASSWORD': secrets.DB_PASSWORD
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
