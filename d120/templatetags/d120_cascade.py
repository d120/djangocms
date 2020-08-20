from django import template

register = template.Library()


@register.filter
def to_todo_item_list(items_str):
    """
    Transfer to do item list encoded as a single newline-separated string
    into a list of entries that can be used in the template
    """
    return [{"id": f"todo-item-{i.replace(' ', '-')}", "label": i} for i in items_str.splitlines()]
