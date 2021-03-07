from django import template
from oilapp.models import Viscosity

register = template.Library()

@register.simple_tag(name="get_viscosities")
def get_viscosities():
    viscosities = Viscosity.objects.all()
    return viscosities