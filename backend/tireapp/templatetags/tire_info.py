from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag(name="get_tire_info")
def get_tire_info(obj):
    return render_to_string("tire/tire-info.html", context={
        'object': obj
    })