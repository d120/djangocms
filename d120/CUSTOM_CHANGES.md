# Custom Changes


## Notes on Localization

When creating custom stuff for the CMS, it might happen that one introduces strings that should be translated for multiple languages. When doing so, remember to execute `manage.py makemessages` and translate the relevant `.po` files unter `locale/`.


## PageTitleModifier

The menu system that is usable in templates does not have access to all attributes of a page by default. In order to be able to retrieve the `page_title` attribute (as opposed to the possibly different menu title) within the menu system, a custom navigation modifier is used.

- `D120NavigationModifier` in `cms_menus.py` makes the `page_title` attribute accessible for the menu system.


## PageColorExtension

In order to be able to assign different accent colors to different pages, a CMS PageExtension is created.

- `PageColorExtension` in `models.py` holds the necessary properties of the extension and defines a tuple of possible colors as well as the default color.
- `PageColorExtensionAdmin` in `admin.py` registers this extension to the admin menu (which is necessary for the extension to work out).
- `PageColorExtensionToolbar` in `cms_toolbars.py` adds an entry to the toolbar in order to modify this attribute.
- `templatetags/page_color.py` defines a templatetag that takes a page and retrieves the page color for this page or one of the parent pages. This makes the page color accessible for the template language.


## MenuEntryMarginExtension

To allow additional spacing between menu entries, a CMS PageExtension is created.

- `MenuEntryMarginExtension` in `models.py` has an attribute that stores if a menu entry should have an additional margin.
- `MenuEntryMarginExtensionAdmin` in `admin.py` registers this extension to the admin menu (which is necessary for the extension to work out).
- `MenuEntryMarginExtensionToolbar` in `cms_toolbars.py` adds an entry to the toolbar in order to modify this attribute.
- `D120NavigationModifier` in `cms_menus.py` makes this custom attribute accessible for the somewhat special menu system.


## MenuEntryHeadlineExtension

Maybe one wants to show additional text above certain menu entries. To be able to add headlines to menu entries, a CMS TitleExtension is created.

- `MenuEntryHeadlineExtension` in `models.py` allows to store a localizable headline for a page's menu entry.
- `MenuEntryHeadlineExtensionAdmin` in `admin.py` registers this extension to the admin menu (which is necessary for the extension to work out).
- `MenuEntryHeadlineExtensionToolbar` in `cms_toolbars.py` adds an entry to the toolbar in order to modify this attribute.
- `D120NavigationModifier` in `cms_menus.py` makes this custom attribute accessible for the somewhat special menu system.


## Templatefilter `unescape_unicode`

The rssplugin may sanitize a RSS feed before passing it to the template but this is not guaranteed, so autoescaping should not be turned off. Unfortunately, feeds can contain unicode entities (e.g. `&#8216;`) that are afterwards escaped by Django (e.g. `&amp;#8216;`). A templatefilter reverts this unwanted escaping.

- `templatetags/unescape_unicode.py` contains the templatefilter that unescapes escaped unicode entities.
