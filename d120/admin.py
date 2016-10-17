from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from d120.models import PageColorExtension


class PageColorExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(PageColorExtension, PageColorExtensionAdmin)
