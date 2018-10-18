"""
This is the settings file used for development.
Beside that, it is imported from the production settings file.
"""

import os


### VARIABLES ###

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


### SECURITY ###

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = '92i^_tl8hjz&7%olbv52d@n%--v3k&l0l6tx)3p8&r(9d@$mry'

CSRF_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


### COMMON DJANGO SETTINGS ###

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_redirect',
    'djangocms_history',
    'aldryn_bootstrap3',
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'rssplugin',
    'sslserver',
    'import_export',
    'bootstrap3',
    'd120',
    'pyTUID',
    'pyBuchaktion',
    'git_version',
    'djangocms_blog',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'djangocms_redirect.middleware.RedirectMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'pyTUID.middleware.TUIDMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'd120', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

ROOT_URLCONF = 'd120.urls'

WSGI_APPLICATION = 'd120.wsgi.application'

SITE_ID = 1
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

### DATABASE ###

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
    }
}


### I18N & L10N ###

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('de', 'de'),
    ('en', 'en'),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'de',
        },
        {
            'code': 'en',
            'name': 'en',
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'hide_untranslated': False,
        'public': True,
    },
}


### STATIC FILES ###

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    ("vendor", "node_modules"),
)


### CACHE ###

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


### MAIL ###

EMAIL_SUBJECT_PREFIX = "[DJANGOCMS] "

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


### COMMON CMS SETTINGS ###

CMS_TEMPLATES = (
    ('frontpage.html', 'Front Page'),
    ('widepage.html', 'Wide Page'),
    ('standardpage.html', 'Standard Page'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}


### FILER ###

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True


### RSSPLUGIN ###

CMS_RSS_PLUGIN_TEMPLATE = 'rss_feed.html'


### PYTUID ###

TUID_SERVER_URL = 'https://sso.tu-darmstadt.de/'
TUID_FORCE_SERVICE_URL = 'https://localhost:8000/tuid/login/'

# application-specific-cookies
CSRF_COOKIE_NAME = 'djangocms_csrftoken'
SESSION_COOKIE_NAME = 'djangocms_sessionid'

### DJANGOCMS BLOG ###

PARLER_LANGUAGES = {
  1: (
    {'code': 'de',},
    {'code': 'en',},
  ),
  'default': {
    'fallbacks': ['en', 'it', 'fr'],
  }
}
