from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar

from d120.models import PageColorExtension, MenuEntryMarginExtension, MenuEntryHeadlineExtension


@toolbar_pool.register
class CustomBreakExtensionToolbar(ExtensionToolbar):
    """Insert a break line in the toolbar menu to visually separate our custom entries.
    """
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            current_page_menu.add_break("custom_break")


@toolbar_pool.register
class PageColorExtensionToolbar(ExtensionToolbar):
    """Add an entry for the PageColorExtension to the toolbar.
    """
    model = PageColorExtension
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(_("Page Color"), url=url, disabled=not self.toolbar.edit_mode_active)


@toolbar_pool.register
class MenuEntryMarginExtensionToolbar(ExtensionToolbar):
    """Add an entry for the MenuEntryMarginExtension to the toolbar.
    """
    model = MenuEntryMarginExtension
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(_("Menu Entry Margin"), url=url, disabled=not self.toolbar.edit_mode_active)


@toolbar_pool.register
class MenuEntryHeadlineExtensionToolbar(ExtensionToolbar):
    """Add an entry for the MenuEntryHeadlineExtension to the toolbar.
    """
    model = MenuEntryHeadlineExtension
    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu and self.toolbar.edit_mode_active:
            sub_menu = self._get_sub_menu(current_page_menu, 'menuentryheadline_menu', _("Menu Entry Headline"))
            urls = self.get_title_extension_admin()
            for title_extension, url in urls:
                sub_menu.add_modal_item(_("Headline for %(title)s") % {"title": self._get_page().get_title()}, url=url, disabled=not self.toolbar.edit_mode_active)
