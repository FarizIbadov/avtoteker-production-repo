from import_export.widgets import Widget
from .models import Brand,Serie

class CustomModelWidget(Widget):
    def __init__(self,model):
        self.model = model

    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
        instance, _ = self.model.objects.get_or_create(title=title)
        return instance

class CustomBrandWidget(Widget):
    def clean(self,value,row=None,*args,**kwargs):
        title = value.strip()
        brand = Brand.objects.get(title=title)
        return brand

class CustomSerieWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
        serie = Serie.objects.get(title=title)
        return serie