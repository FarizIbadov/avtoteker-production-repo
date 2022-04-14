import django_filters

from .models import Tire

class TireFilter(django_filters.FilterSet):
    width = django_filters.CharFilter(field_name="size__width")
    height = django_filters.CharFilter(field_name="size__height")
    radius = django_filters.CharFilter(field_name="size__radius")

    class Meta:
        model = Tire
        fields = ("width", "height", "radius")