from django import template
from oilapp.models import Oil

register = template.Library()

@register.simple_tag(name="get_viscosities")
def get_viscosities():
    viscosities = Oil.objects.available().values_list('viscosity', flat=True).distinct()
    return viscosities