from import_export.widgets import  Widget
from .models import Brand

class CustomBrandWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        title = value.strip()
        brand = Brand.objects.get(title=title)
        return brand

class CustomCharWidget(Widget):
    def clean(self,value,row=None,*args,**kwargs):
        if isinstance(value,float):
            return str(int(value))
        return str(value)
