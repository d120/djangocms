"""
This is the settings file used in production.
First, it imports all default settings, then overrides respective ones.
Secrets are stored in and imported from an additional file, not set under version control.
"""

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

from d120.settings import *
import d120.settings_secrets as secrets


### SECURITY ###

DEBUG = False

ALLOWED_HOSTS = ['.fachschaft.informatik.tu-darmstadt.de', '.d120.de']

SECRET_KEY = secrets.SECRET_KEY

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


### DATABASE ###

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'djangocms',
        'USER': 'djangocms',
        'PASSWORD': secrets.DB_PASSWORD,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


### CACHE ###

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'KEY_PREFIX': 'd120-djangocms',
    }
}


### AUTHENTICATION & LDAP ###

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://10.162.32.200"
AUTH_LDAP_BIND_DN = 'cn=djangocms,ou=Services,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de'
AUTH_LDAP_BIND_PASSWORD = secrets.LDAP_PASSWORD
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de", ldap.SCOPE_ONELEVEL, "(uid=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de", ldap.SCOPE_ONELEVEL, "(objectClass=groupOfNames)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_REQUIRE_GROUP = "cn=fachschaft,ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de"

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=fachschaft,ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de",
    "is_staff": "cn=fachschaft,ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de",
    "is_superuser": "cn=fss,ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de",
}


### MAIL ###

ADMINS = [
    ('UA-Webseite', 'webseite@fachschaft.informatik.tu-darmstadt.de'),
]

MANAGERS = [
    ('UA-Webseite', 'webseite@fachschaft.informatik.tu-darmstadt.de'),
]

SERVER_EMAIL = "djangocms@fachschaft.informatik.tu-darmstadt.de"
DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.d120.de'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'djangocms'
EMAIL_HOST_PASSWORD = secrets.MAIL_PASSWORD


### PYTUID ###

TUID_SERVER_URL = 'https://sso.tu-darmstadt.de'
TUID_FORCE_SERVICE_URL = 'https://www.fachschaft.informatik.tu-darmstadt.de/tuid/login/'

### SERVICE MENU ###

SITE_URL = 'https://www.fachschaft.informatik.tu-darmstadt.de'
BLOG_URL = 'https://daswesentliche.fachschaft.informatik.tu-darmstadt.de'
