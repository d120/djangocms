from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from d120.models import PageColorExtension, MenuEntryMarginExtension


class PageColorExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(PageColorExtension, PageColorExtensionAdmin)


class MenuEntryMarginExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(MenuEntryMarginExtension, MenuEntryMarginExtensionAdmin)
