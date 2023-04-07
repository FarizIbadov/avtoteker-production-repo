from django import template

from main_site import models

register = template.Library()

@register.simple_tag(name="get_tire_bottom_icons")
def get_tire_bottom_icons():
    return models.TireBottomIcons.objects.filter(active=True).first()
     