"""
This is the settings file used for development.
Beside that, it is imported from the production settings file.
"""

import os


### VARIABLES ###
from django.urls import reverse_lazy
from django.utils.text import format_lazy

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
    'djangocms_redirect',
    'djangocms_history',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
#    'djangocms_forms',
    'django_select2',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'rssplugin',
    'sslserver',
    'd120',
    'git_version',
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',  # optional
    'cmsplugin_cascade.extra_fields',  # optional
    'cmsplugin_cascade.sharable',  # optional
    'cmsplugin_cascade.segmentation',  # optional
)

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'djangocms_redirect.middleware.RedirectMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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
]

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
#                'django.template.loaders.eggs.Loader',
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
    ('standardpage.html', 'Standard Page'),
    ('plain.html', 'Plain Page'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'content': {
        'parent_classes': {'BootstrapContainerPlugin': None,},
    },
}

### FILER ###

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True


### RSSPLUGIN ###

CMS_RSS_PLUGIN_TEMPLATE = 'rss_feed.html'

### CASCADE ###

CMSPLUGIN_CASCADE_PLUGINS = ['cmsplugin_cascade.bootstrap4']
CMSPLUGIN_CASCADE_PLUGINS.append('cmsplugin_cascade.generic')
CMSPLUGIN_CASCADE_PLUGINS.append('d120')

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono-lisa',
    'toolbar': 'CMS',
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texteditor_config')),
    'contentsCss': [
        '/static/vendor/bootstrap/dist/css/bootstrap.min.css',
        '/static/vendor/font-awesome/css/font-awesome.min.css',
        '/static/vendor/fontsource-libre-franklin/index.css',
        '/static/d120/css/custom.css',
    ],
}

CMSPLUGIN_CASCADE = {
    'plugins_with_extra_render_templates': {
            'CustomSnippetPlugin': [
                # other tuples
            ],
        },
    'alien_plugins': ['TextPlugin'],
}

# application-specific-cookies
CSRF_COOKIE_NAME = 'djangocms_csrftoken'
SESSION_COOKIE_NAME = 'djangocms_sessionid'

### ICONS ###

DJANGOCMS_ICON_SETS = (
    ('fontawesome4', 'fa', 'Font Awesome 4', 'lastest'),
)
