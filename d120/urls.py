# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import django.contrib.sitemaps.views

admin.autodiscover()

urlpatterns = [
#        url(r'', include('djangocms_forms.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('sitemap.xml', django.contrib.sitemaps.views.sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    path('select2/', include('django_select2.urls')),
#    url(r'tuid/', include('pyTUID.urls')),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    import django.views.static
    urlpatterns = [
        re_path(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
