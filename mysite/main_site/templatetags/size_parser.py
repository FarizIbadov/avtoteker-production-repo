from django import template

from tireapp.models import Size
from  specific.models import Brand

register = template.Library()


@register.simple_tag(name="parse_size")
def parse_size(request):
    width_text = "en"
    width_def = ""
    if request.GET.get('width'):
        width_def = request.GET.get('width')

    height_text = "hündürlük"
    height_def = ""
    if request.GET.get('height'):
        height_def = request.GET.get('height')

    radius_text = "radius"
    radius_def = ""
    if request.GET.get('radius'):
        radius_def = request.GET.get('radius')

    width_obj = SizeField("width",width_text,width_def)
    height_obj = SizeField("height",height_text,height_def)
    radius_obj = SizeField("radius",radius_text,radius_def)
    return (width_obj, height_obj, radius_obj)


class SizeField:
    queryset = Size.objects.all()

    def __init__(self, field,name,default=""):
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
