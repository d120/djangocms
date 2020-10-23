from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.fields import SizeField
from cmsplugin_cascade.plugin_base import CascadePluginBase, TransparentContainer
from django.forms import CharField, Textarea, ChoiceField, IntegerField, FloatField
from entangled.forms import EntangledModelFormMixin


class ToDoListFormMixin(EntangledModelFormMixin):
    heading = CharField(initial="ToDo")
    prefix = CharField(help_text="Make sure the items do not collide with another ToDoList on this page")
    items = CharField(widget=Textarea, help_text="Add one to do item per line")

    class Meta:
        entangled_fields = {'glossary': ['heading', 'prefix', 'items']}


class ToDoListPlugin(CascadePluginBase):
    """
    Plugin to show a simple to do list that stores its current state in the local browser storage
    """
    name = 'ToDo List'
    render_template = 'plugins/todo_list.html'
    form = ToDoListFormMixin

    @classmethod
    def get_identifier(cls, instance):
        return instance.glossary["heading"]


plugin_pool.register_plugin(ToDoListPlugin)


class ChangelogBoxPlugin(TransparentContainer, CascadePluginBase):
    """
    Plugin to show the last change (publication) timestamp of this page
    (together with other plugins indicating the changes if wanted)
    """
    name = 'Changelog Box'
    render_template = 'plugins/changelog.html'
    allow_children = True


plugin_pool.register_plugin(ChangelogBoxPlugin)


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
    Plugin representing an entry of the timeline plugin
    """
    name = 'Timeline Entry'
    render_template = 'plugins/timeline_entry.html'
    form = TimelineEntryFormMixin
    allow_children = True
    parent_classes = ["TimelinePlugin"]
    require_parent = True

    @classmethod
    def get_identifier(cls, instance):
        return instance.glossary["header"]


plugin_pool.register_plugin(TimelineEntryPlugin)


class MapFormMixin(EntangledModelFormMixin):
    height = SizeField(help_text="Height of the map")
    lon = CharField(help_text="Longitude of center", label="Longitude")
    lat = CharField(help_text="Latitude of center", label="Latitude")
    zoom = IntegerField(help_text="Zoomlevel of map")
    layers = CharField(widget=Textarea, help_text="One Layer identifier (no blanks) per line. Should be human-readable.")

    class Meta:
        entangled_fields = {'glossary': ['height', 'lon', 'lat', 'zoom', 'layers']}


class MapPlugin(CascadePluginBase):
    """
    Embed a custom open street map in the page

    Due to limitations in the django cascade plugin system, only one map can be used per page
    and after editing the page has to be reloaded to reflect the changes.
    """
    name = 'Map'
    render_template = 'plugins/map.html'
    form = MapFormMixin
    allow_children = True


plugin_pool.register_plugin(MapPlugin)


class MapMarkerEntryFormMixin(EntangledModelFormMixin):
    title = CharField(help_text="Short title")
    layer = CharField(help_text="Layer")
    lon = CharField(label="Longitude")
    lat = CharField(label="Latitude")
    description = CharField(widget=Textarea)
    icon = ChoiceField(
        choices=[('5', 'Blue'), ('6', 'Red'), ('7', 'Green'), ('8', 'Purple'), ('9', 'Turquoise'), ('10', 'Orange'), ('11', 'House')],
        label="Icon",
        initial='5',
        help_text="Icon of this marker"
    )

    class Meta:
        entangled_fields = {'glossary': ['title', 'layer', 'lon', 'lat', 'description', 'icon']}


class MapMarkerPlugin(CascadePluginBase):
    """
    Plugin to add a marker to the map plugin
    """
    name = 'Map Marker'
    render_template = 'plugins/map_marker.html'
    form = MapMarkerEntryFormMixin
    allow_children = False
    require_parent = True
    parent_classes = ["MapPlugin"]
    require_parent = True

    @classmethod
    def get_identifier(cls, instance):
        return instance.glossary["title"]


plugin_pool.register_plugin(MapMarkerPlugin)


class CustomCSSBlockFormMixin(EntangledModelFormMixin):
    css = CharField(widget=Textarea)

    class Meta:
        entangled_fields = {'glossary': ['css']}


class CustomCSSBlockPlugin(CascadePluginBase):
    """
    Plugin to add a marker to the map plugin
    """
    name = 'Custom CSS Block'
    render_template = 'plugins/css_block.html'
    form = CustomCSSBlockFormMixin
    allow_children = False

    @classmethod
    def get_identifier(cls, instance):
        return instance.glossary['css']


plugin_pool.register_plugin(CustomCSSBlockPlugin)
