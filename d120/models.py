from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class PageColorExtension(PageExtension):
    """PageExtension which adds a color property to pages.
    """
    class Meta:
        verbose_name = _("Page Color")
        verbose_name_plural = _("Page Colors")
    PAGE_COLORS = (
        ("#d35400", _("Orange")),
        ("#c0392b", _("Red")),
        ("#8e44ad", _("Purple")),
        ("#2980b9", _("Blue")),
        ("#16a085", _("Turquoise")),
        ("#27ae60", _("Green")),
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
