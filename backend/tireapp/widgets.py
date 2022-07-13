from import_export.widgets import BooleanWidget, Widget, FloatWidget
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
        brand = Brand.objects.filter(title=title).first()
        
        if not brand:
            brand = Brand.objects.create(title=title)

        return brand


class CustomSerieWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        brand_title = row['brand'].strip()
        brand = Brand.objects.filter(title=brand_title).first()
        
        if not brand:
            brand = Brand.objects.create(title=brand_title)

        serie = Serie.objects.filter(
            title=value,
            brand=brand
        ).first()

        if not serie:
            serie = Serie.objects.create(
                title=value,
                brand=brand
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
        if value == '-' or value == None:
            return None
            
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

