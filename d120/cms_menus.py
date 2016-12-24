from django.utils.translation import get_language
from cms.models import Title
from menus.base import Modifier
from menus.menu_pool import menu_pool


class D120NavigationModifier(Modifier):
    """Make several useful attributes accessible for the menu system.
    - the page_title attribute
    - the custom MenuEntryMarginExtension
    - the custom MenuEntryHeadlineExtension
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):

        if breadcrumb:
            language = get_language()
            # take the nodes relevant for the breadcrumb
            selected_node = next(n for n in nodes if n.selected and n.attr["is_page"])
            page_nodes = [selected_node] + selected_node.get_ancestors()
            nodes_by_id = {n.id: n for n in page_nodes}
            # fetch relevant fields from the database
            titles = Title.objects.filter(page_id__in=[n.id for n in page_nodes]).values('page_id', 'language', 'page_title', 'title')

            for t in titles:
                node = nodes_by_id[t['page_id']]
                # make the page_title attribute accessible for the breadcrumb
                if language == t['language'] or 'page_title' not in node.attr:
                    node.attr['page_title'] = t['page_title'] if t['page_title'] else t['title']

        elif post_cut:
            language = get_language()
            # take the nodes relevant for the menu
            page_nodes = [n for n in nodes if n.attr["is_page"]]
            nodes_by_id = {n.id: n for n in page_nodes}
            # fetch relevant fields from the database
            titles = Title.objects.filter(page_id__in=[n.id for n in page_nodes]).values('page_id', 'language', 'page__menuentrymarginextension__additional_margin', 'menuentryheadlineextension__headline')

            for t in titles:
                node = nodes_by_id[t['page_id']]
                # make the custom MenuEntryMarginExtension accessible for the menu
                node.attr['additional_margin'] = t['page__menuentrymarginextension__additional_margin']

                # make the custom MenuEntryHeadlineExtension accessible for the menu
                if t['menuentryheadlineextension__headline'] and (language == t['language'] or 'headline' not in node.attr):
                    node.attr['headline'] = t['menuentryheadlineextension__headline']

        return nodes

menu_pool.register_modifier(D120NavigationModifier)
