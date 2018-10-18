import hashlib
from django import template

register = template.Library()

@register.simple_tag
def gravatar_url(email):
    bytes = email.lower().encode('utf-8')
    hash = hashlib.md5(bytes).hexdigest()
    print(hash)
    return "https://www.gravatar.com/avatar/{0}".format(hash)
