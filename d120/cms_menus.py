from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page


class MenuEntryMarginModifier(Modifier):
    """Make the additional menu entry margin accessible for the menu.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        for node in nodes:
            if node.attr["is_page"]:
                page = Page.objects.get(id=node.id)
                if hasattr(page, "menuentrymarginextension"):
                    node.attr["additional_margin"] = page.menuentrymarginextension.additional_margin
                else:
                    node.attr["additional_margin"] = False
        return nodes

menu_pool.register_modifier(MenuEntryMarginModifier)
