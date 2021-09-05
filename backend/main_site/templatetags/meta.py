from django import template
from metaapp.models import Meta

register = template.Library()

@register.simple_tag(name="get_meta")
def get_meta():
    meta_obj = Meta.objects.filter(active=True).first()
    if meta_obj:
        return meta_obj.content
    else:
        return ""