from django import template
from adds.models import Add

register = template.Library()

@register.simple_tag(name="get_slider")
def get_slider():
    adds = Add.objects.filter(active=True).exclude(image__isnull=True)
    return adds