from django import template

from main_site.models import TireListMessage

register = template.Library()

@register.simple_tag(name="get_price_3_text")
def get_price_3_text():
    return TireListMessage.objects.filter(active=True).first()