from django import template

register = template.Library()


@register.simple_tag(name="url_encoder")
def url_encoder(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)
    return "?" + updated.urlencode()

@register.simple_tag(name="get_paginator_url")
def get_paginator_url(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)
    return "?" + updated.urlencode()


@register.simple_tag(name="get_region_path")
def get_region_path(request,language_code):
    path_items = list(filter(None,request.path.split('/')))
    path_items[0] = language_code
    query = get_paginator_url(request)
    return  '/' + "/".join(path_items) + query