from django import template
from oilapp.models import Brand

register = template.Library()

@register.simple_tag(name="get_oil_brands")
def get_oil_brands():
    brands = Brand.objects.filter(show_in_slider=True)
    return brands