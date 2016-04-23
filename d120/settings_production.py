"""
This is the settings file used in production.
First, it imports all default settings, then overrides respective ones.
Secrets are stored in and imported from an additional file, not set under version control.
"""

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

from d120.settings import *
import d120.settings_secrets as secrets

SECRET_KEY = secrets.SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['.fachschaft.informatik.tu-darmstadt.de', '.d120.de']

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

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://10.162.32.201"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=People,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de"
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=fachschaft,dc=informatik,dc=tu-darmstadt,dc=de", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")
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
