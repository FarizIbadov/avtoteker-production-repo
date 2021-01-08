from django import template

from tireapp.models import Size
from  specific.models import Brand

register = template.Library()


@register.simple_tag(name="parse_size")
def parse_size():
    width_obj = SizeField("width","en")
    height_obj = SizeField("height","hündürlük")
    radius_obj = SizeField("radius","radius")
    return (width_obj, height_obj, radius_obj)

@register.simple_tag(name="get_brand")
def get_brand():
    return Brand.objects.all()


class SizeField:
    queryset = Size.objects.all()

    def __init__(self, field,name):
        self.field = field
        self.name = name
        self.list = self.get_field_list()

    def get_field_list(self):
        return list(
            self.queryset.values_list(self.field, flat=True)
            .distinct()
            .order_by(self.field)
        )
