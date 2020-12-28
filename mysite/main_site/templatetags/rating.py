from django import template

register = template.Library()

@register.filter(name='get_rating')
def get_rating(value):
    templates = []
    for i in range(int(value)):
        templates.append("<span class='active'></span>")
    if not len(templates) == 5:
        remain = 5 - len(templates)
        for i in range(remain):
            templates.append("<span></span>")
    return "".join(templates)

"""
<span class='active'></span>
<span></span>
"""