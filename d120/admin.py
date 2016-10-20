from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from d120.models import PageColorExtension, MenuEntryMarginExtension


@admin.register(PageColorExtension)
class PageColorExtensionAdmin(PageExtensionAdmin):
    pass


@admin.register(MenuEntryMarginExtension)
class MenuEntryMarginExtensionAdmin(PageExtensionAdmin):
    pass
