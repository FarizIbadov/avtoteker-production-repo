from django import template
from navigation.models import NavigationLink

register = template.Library()

@register.simple_tag(name="get_navigation_list")
def get_navigation_list():
    return NavigationLink.objects.filter(deleted=False)
