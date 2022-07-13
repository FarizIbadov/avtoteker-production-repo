from django import template
from main_site.models import ManatIcon

register = template.Library()

@register.simple_tag(name="get_manat_icon")
def get_manat_icon():
    return ManatIcon.objects.filter(active=True).first()