from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar

from d120.models import PageColorExtension, MenuEntryMarginExtension


@toolbar_pool.register
class PageColorExtensionToolbar(ExtensionToolbar):
    model = PageColorExtension
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(_("Page Color"), url=url, disabled=not self.toolbar.edit_mode)


@toolbar_pool.register
class MenuEntryMarginExtensionToolbar(ExtensionToolbar):
    model = MenuEntryMarginExtension
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(_("Menu Entry Margin"), url=url, disabled=not self.toolbar.edit_mode)
