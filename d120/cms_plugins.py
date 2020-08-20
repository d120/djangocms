from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.plugin_base import CascadePluginBase
from django.forms import CharField, Textarea
from entangled.forms import EntangledModelFormMixin


class ToDoListFormMixin(EntangledModelFormMixin):
    items = CharField(widget=Textarea, help_text="Add one to do item per line")

    class Meta:
        entangled_fields = {'glossary': ['items']}


class ToDoListPlugin(CascadePluginBase):
    """
    Plugin to show a simple to do list that stores its current state in the local browser storage
    """
    name = 'ToDo List'
    render_template = 'plugins/todo_list.html'
    form = ToDoListFormMixin


plugin_pool.register_plugin(ToDoListPlugin)
