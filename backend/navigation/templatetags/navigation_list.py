from django import template
from navigation import models 

register = template.Library()

@register.simple_tag(name="get_navigation_list")
def get_navigation_list():
    return models.NavigationLink.objects.filter(active=True).exclude(title__isnull=True)

@register.simple_tag(name="get_logo")
def get_logo():
    return models.Logo.objects.filter(active=True).first()