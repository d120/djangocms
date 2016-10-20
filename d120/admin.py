from django.contrib import admin

from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin

from d120.models import PageColorExtension, MenuEntryMarginExtension, MenuEntryHeadlineExtension


@admin.register(PageColorExtension)
class PageColorExtensionAdmin(PageExtensionAdmin):
    pass


@admin.register(MenuEntryMarginExtension)
class MenuEntryMarginExtensionAdmin(PageExtensionAdmin):
    pass


@admin.register(MenuEntryHeadlineExtension)
class MenuEntryHeadlineExtensionAdmin(TitleExtensionAdmin):
    pass
