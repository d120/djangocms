from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Title


class D120NavigationModifier(Modifier):
    """Make several useful attributes accessible for the menu system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):

        if breadcrumb:
            selected = next(n for n in nodes if n.selected and n.attr["is_page"])
            page_nodes = [selected] + selected.get_ancestors()
            titles = {t.page_id: t for t in Title.objects.filter(page_id__in=[n.id for n in page_nodes])}
            for node in page_nodes:
                # make the page_title attribute accessible for the breadcrumb
                node.attr["page_title"] = titles[node.id].page_title if titles[node.id].page_title else titles[node.id].title

        elif post_cut:
            page_nodes = [n for n in nodes if n.attr["is_page"]]
            titles = {t.page_id: t for t in Title.objects.filter(page_id__in=[n.id for n in page_nodes]).select_related('page__menuentrymarginextension', 'menuentryheadlineextension')}
            for node in page_nodes:
                title = titles[node.id]
                page = title.page

                # make the custom MenuEntryMarginExtension accessible for the menu
                if hasattr(page, "menuentrymarginextension"):
                    node.attr["additional_margin"] = page.menuentrymarginextension.additional_margin

                # make the custom MenuEntryHeadlineExtension accessible for the menu
                if hasattr(title, "menuentryheadlineextension"):
                    node.attr["headline"] = title.menuentryheadlineextension.headline

        return nodes

menu_pool.register_modifier(D120NavigationModifier)
