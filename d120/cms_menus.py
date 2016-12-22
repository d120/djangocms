from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page


class D120NavigationModifier(Modifier):
    """Make several useful attributes accessible for the menu system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):

        if breadcrumb:
            selected = next(n for n in nodes if n.selected and n.attr["is_page"])
            page_nodes = [selected] + selected.get_ancestors()
            pages = Page.objects.filter(id__in=[n.id for n in page_nodes])
            for node in page_nodes:
                # make the page_title attribute accessible for the breadcrumb
                node.attr["page_title"] = pages.get(id=node.id).get_page_title()

        elif post_cut:
            page_nodes = [n for n in nodes if n.attr["is_page"]]
            pages = Page.objects.filter(id__in=[n.id for n in page_nodes])
            for node in page_nodes:
                page = pages.get(id=node.id)

                # make the custom MenuEntryMarginExtension accessible for the menu
                if hasattr(page, "menuentrymarginextension"):
                    node.attr["additional_margin"] = page.menuentrymarginextension.additional_margin

                # make the custom MenuEntryHeadlineExtension accessible for the menu
                title_obj = page.get_title_obj()
                if hasattr(title_obj, "menuentryheadlineextension"):
                    node.attr["headline"] = title_obj.menuentryheadlineextension.headline

        return nodes

menu_pool.register_modifier(D120NavigationModifier)
