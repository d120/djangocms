import bleach as bleach
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def to_todo_item_list(items_str, prefix):
    """
    Transfer to do item list encoded as a single newline-separated string
    into a list of entries that can be used in the template
    """
    return [{"id": f"todo-item-{prefix}--{i.replace(' ', '-')}", "label": i} for i in items_str.splitlines()]


@register.filter
def multiline_to_items(items_str):
    return items_str.splitlines()


@register.filter
def partially_safe(midsafe_string):
    """
    Clean string from everything not allowed by default by bleach lib
    and mark the resulting string as safe
    """
    return mark_safe(bleach.clean(midsafe_string))
