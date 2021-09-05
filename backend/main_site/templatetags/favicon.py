from django import template
from faviconapp.models import Favicon

register = template.Library()

@register.simple_tag(name='get_favicon')
def get_favicon():
    favicon_obj = Favicon.objects.filter(active=True).first()
    if favicon_obj:
        return favicon_obj.icon.url
    else:
        return ""
