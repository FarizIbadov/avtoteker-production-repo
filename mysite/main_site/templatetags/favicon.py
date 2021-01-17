from django import template
from faviconapp.models import Favicon

register = template.Library()

@register.simple_tag(name='get_favicon')
def get_favicon():
    favicon_obj = Favicon.objects.get(active=True)
    return favicon_obj
