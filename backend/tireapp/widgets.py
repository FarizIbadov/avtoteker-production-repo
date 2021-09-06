from import_export.widgets import BooleanWidget, Widget, DecimalWidget
from specific.models import Brand, Serie, Country, Season
from .models import Size, TireClass


class CustomBooleanWidget(BooleanWidget):
    def render(self, value, obj=None):
        return "+" if value else "-"

    def clean(self, value, row=None, *args, **kwargs):
        return value == "+"


class CustomBrandWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
<<<<<<< HEAD:backend/tireapp/widgets.py
        brand, _ = Brand.objects.get_or_create(title=title)
=======
        brand = Brand.objects.get(title=title)
>>>>>>> ac0f46f91bcac003dc6bf55f295bd575af0870a5:mysite/tireapp/widgets.py
        return brand


class CustomSerieWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
<<<<<<< HEAD:backend/tireapp/widgets.py
        serie, _ = Serie.objects.get_or_create(
=======
        serie = Serie.objects.get(
>>>>>>> ac0f46f91bcac003dc6bf55f295bd575af0870a5:mysite/tireapp/widgets.py
            title=value
        )
        return serie


class CustomCountryWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
        country, _ = Country.objects.get_or_create(title=title)
        return country


class CustomClassWidget(Widget):
    def render(self, value, obj=None):
        return value.title
      

    def clean(self, value, row=None, *args, **kwargs):
        tire_class, _ = TireClass.objects.get_or_create(title=value.strip())
        return tire_class


class CustomSizeWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        width, height, radius = str(value).strip().split("\\")
        size, _ = Size.objects.get_or_create(width=width, height=height, radius=radius)
        return size


class CustomSeasonWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        season, _ = Season.objects.get_or_create(title=value)
        return season


class CustomDecimalWidget(DecimalWidget):
    def __init__(self, month):
        self.month = month

    def clean(self, value, row=None, *args, **kwargs):
        new_value = super().clean(value)
        if not new_value:
            if row.get("sale"):
                new_value = row["sale"] / self.month
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

