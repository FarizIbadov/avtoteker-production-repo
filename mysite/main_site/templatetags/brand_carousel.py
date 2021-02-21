from django import template
from specific.models import Brand

register = template.Library()

@register.simple_tag(name="get_brands")
def get_brands():
    brands = Brand.objects.filter(show_in_slider=True)
    return brands