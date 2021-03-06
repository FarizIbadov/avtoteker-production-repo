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
        title = value.strip()
        brand = Brand.objects.get(title=title)
        return brand


class CustomSerieWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        serie = Serie.objects.get(
            title=value
        )
        return serie


class CustomCountryWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
        country = Country.objects.get(title=title)
        return country


class CustomClassWidget(Widget):
    def render(self, value, obj=None):
        Classes = {"1": "Econom", "2": "Orta", "3": "Premium"}
        key = str(value).strip()
        return Classes[key]

    def clean(self, value, row=None, *args, **kwargs):
        Classes = {"Econom": 1, "Orta": 2, "Premium": 3}
        cap_word = value.strip()
        index = Classes.get(cap_word, 2)
        return index


class CustomSizeWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        width, height, radius = str(value).strip().split("\\")
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


class CustomOutletBooleanWidget(CustomBooleanWidget):
    def render(self, value, obj=None):
        return super().render(value, obj=None)

    def clean(self, value, row=None, *args, **kwargs):
        new = row.get('new').strip()
        if not value and new == "+":
            return False
        if not value and new == "-":
            return True
        return value == "+"

class CustomNewBooleanWidget(CustomBooleanWidget):
    def render(self, value, obj=None):
        return super().render(value, obj=None)

    def clean(self, value, row=None, *args, **kwargs):
        outlet = row.get('outlet').strip()
        if not value and outlet == "+":
            return False
        if not value and outlet == "-":
            return True
        return value == "+"

