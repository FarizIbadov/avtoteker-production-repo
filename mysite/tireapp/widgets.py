from import_export.widgets import BooleanWidget, Widget, DecimalWidget
from specific.models import Brand, Serie, Country, Season
from .models import Size


class CustomBooleanWidget(BooleanWidget):
    def render(self, value, obj=None):
        return "+" if value else "-"

    def clean(self, value, row=None, *args, **kwargs):
        return value == "+"


class CustomBrandWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        country = row.get("origin")
        title = value
        brand = Brand.objects.get(title=title, country__title=country)
        return brand


class CustomSerieWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        country = row.get("origin")
        brand = row.get("brand")
        serie = Serie.objects.get(
            title=value, brand__title=brand, brand__country__title=country
        )
        return serie


class CustomCountryWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value
        country = Country.objects.get(title=title)
        return country


class CustomClassWidget(Widget):
    def render(self, value, obj=None):
        Classes = {"1": "Econom", "2": "Orta", "3": "Premium"}
        key = str(value)
        return Classes[key]

    def clean(self, value, row=None, *args, **kwargs):
        Classes = {"Econom": 1, "Orta": 2, "Premium": 3}
        cap_word = value
        index = Classes.get(cap_word, 2)
        return index


class CustomSizeWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        width, height, radius = str(value).split("\\")
        size, _ = Size.objects.get_or_create(width=width, height=height, radius=radius)
        return size


class CustomSeasonWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        season = Season.objects.get(title=value)
        return season


class CustomDecimalWidget(DecimalWidget):
    def __init__(self, month):
        self.month = month

    def clean(self, value, row=None, *args, **kwargs):
        new_value = super().clean(value)
        if not new_value:
            if row.get('sale active') == '+':
                new_value = row.get("sale") / self.month
            else:
                new_value = row.get("price") / self.month

        return new_value
