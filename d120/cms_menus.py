from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page


class PageTitleModifier(Modifier):
    """Make the page_title accessible for the menu.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        for node in nodes:
            if node.attr["is_page"]:
                page = Page.objects.get(id=node.id)
                node.attr["page_title"] = page.get_page_title()
        return nodes

menu_pool.register_modifier(PageTitleModifier)


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


class MenuEntryHeadlineModifier(Modifier):
    """Make the menu entry headline accessible for the menu.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        for node in nodes:
            if node.attr["is_page"]:
                title_obj = Page.objects.get(id=node.id).get_title_obj()
                if hasattr(title_obj, "menuentryheadlineextension"):
                    node.attr["headline"] = title_obj.menuentryheadlineextension.headline
        return nodes

menu_pool.register_modifier(MenuEntryHeadlineModifier)
