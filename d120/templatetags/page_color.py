from django import template

from d120.models import PageColorExtension

register = template.Library()

@register.simple_tag
def page_color(page):
    """Template tag which retrieves the color for a given page.
    If a color is specified for the page, it is returned immediately.
    Otherwise, the color of the parent page is used.
    """
    p = page
    while p is not None:
        if hasattr(p, "pagecolorextension"):
            color = p.pagecolorextension.color
            if color:
                return color
        p = p.parent_page
    return PageColorExtension.DEFAULT_COLOR
