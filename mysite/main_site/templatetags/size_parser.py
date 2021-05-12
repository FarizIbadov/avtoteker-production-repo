from django import template
from django.urls import reverse,resolve

from tireapp.models import Size
from  specific.models import Brand

register = template.Library()


@register.simple_tag(name="parse_size")
def parse_size(request):
    size = get_size(request)

    width_def = "" if size[0] == "-" else size[0]
    height_def = "" if size[1] == "-" else size[1]
    radius_def = "" if size[2] == "-" else size[2]

    width_obj = SizeField("width","en",width_def)
    height_obj = SizeField("height","hündürlük",height_def)
    radius_obj = SizeField("radius","radius",radius_def)
    return (width_obj, height_obj, radius_obj)

@register.simple_tag(name="parse_size_for_title")
def parse_size_for_title(request):
    return "%s/%s/%s" % get_size(request)

@register.simple_tag(name="parse_size_for_meta")
def parse_size_for_meta(request):
    return "%s/%s/%s" % get_size(request)
    
@register.simple_tag(name="parse_size_for_list")
def parse_size_for_list(request):
    return "%s/%sR%s" % get_size(request)


@register.simple_tag(name="get_size_action")
def get_size_action(request):
    size = get_size(request)

    if size[0] == "-" and size[1] == "-" and size[2] == "-":
        return reverse("list")

    reversed_url = reverse("detail-list",kwargs={
        "width": "_" if size[0] == "-" else size[0],
        "height": "_" if size[1] == "-" else size[1],
        "radius": "_" if size[2] == "-" else size[2],
    })
    print("Not here")
    return reversed_url

def get_size(request):
    size_dict = {}
    resolved_path = resolve(request.path)

    if resolved_path.url_name == "detail-list":
        size_dict = { **resolved_path.kwargs }

    width = "-" if size_dict.get('width',"_") == "_" else size_dict['width']
    height = "-" if size_dict.get('height',"_") == "_" else size_dict['height']
    radius = "-" if size_dict.get('radius',"_") == "_" else size_dict['radius']

    return (width,height,radius)

class SizeField:
    queryset = Size.objects.all()

    def __init__(self,field,name,default=""):
        self.default = default
        self.field = field
        self.name = name
        self.list = self.get_field_list()

    def get_field_list(self):
        return list(
            self.queryset.values_list(self.field, flat=True)
            .distinct()
            .order_by(self.field)
        )