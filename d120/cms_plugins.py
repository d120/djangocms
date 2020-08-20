from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.plugin_base import CascadePluginBase
from django.forms import CharField, Textarea, ChoiceField
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


class TimelinePlugin(CascadePluginBase):
    """
    Plugin to show a vertical timeline
    """
    name = 'Timeline'
    render_template = 'plugins/timeline.html'
    allow_children = True


plugin_pool.register_plugin(TimelinePlugin)


class TimelineEntryFormMixin(EntangledModelFormMixin):
    header = CharField(help_text="Short header")
    pos = ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right')],
        label="Position",
        initial='left',
        help_text="Left or right of the timeline."
    )

    class Meta:
        entangled_fields = {'glossary': ['header', 'pos']}


class TimelineEntryPlugin(CascadePluginBase):
    """
    Plugin to show a vertical timeline
    """
    name = 'Timeline Entry'
    render_template = 'plugins/timeline_entry.html'
    form = TimelineEntryFormMixin
    allow_children = True


plugin_pool.register_plugin(TimelineEntryPlugin)
