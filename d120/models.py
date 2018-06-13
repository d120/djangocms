from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.extensions import PageExtension, TitleExtension
from cms.extensions.extension_pool import extension_pool


class PageColorExtension(PageExtension):
    """PageExtension which adds a color property to pages.
    """
    class Meta:
        verbose_name = _("Page Color")
        verbose_name_plural = _("Page Colors")
    PAGE_COLORS = (
        ("#CC4C03", _("Orange")),
        ("#B90F22", _("Red")),
        ("#804597", _("Purple")),
        ("#00689D", _("Blue")),
        ("004E73", _("DarkBlue")),
        ("#009D81", _("Turquoise")),
        ("#6A8B22", _("Green")),
    )
    DEFAULT_COLOR = PAGE_COLORS[0][0]
    color = models.CharField(blank=True, choices=PAGE_COLORS, max_length=16, verbose_name=_("Color"))

extension_pool.register(PageColorExtension)


class MenuEntryMarginExtension(PageExtension):
    """PageExtension which allows to enable an additional margin for specific menu entries.
    """
    class Meta:
        verbose_name = _("Menu Entry Margin")
        verbose_name_plural = _("Menu Entry Margins")
    additional_margin = models.BooleanField(default=False, verbose_name=_("Enable additional margin for menu entry"))

extension_pool.register(MenuEntryMarginExtension)


class MenuEntryHeadlineExtension(TitleExtension):
    """TitleExtension which allows to add headlines to specific menu entries.
    """
    class Meta:
        verbose_name = _("Menu Entry Headline")
        verbose_name_plural = _("Menu Entry Headlines")
    headline = models.CharField(blank=True, max_length=64, verbose_name=_("Menu entry headline"))

extension_pool.register(MenuEntryHeadlineExtension)
