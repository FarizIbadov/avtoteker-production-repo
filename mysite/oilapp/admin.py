from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Brand,Serie,Oil
from .resources import OilResource
from .forms import OilForm
from utils.admin import CustomModelAdmin


@admin.register(Brand)
class BrandAdmin(CustomModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(CustomModelAdmin):
    pass

@admin.register(Oil)
class OilAdmin(ImportExportMixin,CustomModelAdmin):
    resource_class = OilResource
    form_class = OilForm


