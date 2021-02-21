from django import template
from copyright.models import Copyright

register = template.Library()

@register.simple_tag(name='get_copyright')
def get_copyright():
    copirigth_obj = Copyright.objects.filter(active=True).first()
    
    if copirigth_obj:
        return copirigth_obj.content
    return ""
