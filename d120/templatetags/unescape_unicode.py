from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
@stringfilter
def unescape_unicode(value, autoescape=True):
    """Template filter that unescapes escaped unicode entities.
    """
    if not autoescape:
        return value
    result = conditional_escape(value)
    result = result.replace('&amp;#', '&#')
    return mark_safe(result)
