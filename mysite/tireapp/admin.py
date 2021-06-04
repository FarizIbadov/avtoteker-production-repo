from django.contrib import admin
from .forms import TireForm
from .models import Tire,Size,OneSTire
from import_export.admin import ImportExportMixin,ImportMixin
from utils.admin import CustomModelAdmin
from .resources import TireResource,  OneSTireResource


@admin.register(Tire)
class TireAdmin(ImportExportMixin,CustomModelAdmin):
    form = TireForm
    resource_class = TireResource
    exclude = ("size",)
    list_display = ["brand", "serie", "size", "manufacturer","quantity"]
    list_filter = ["brand", "serie", "manufacturer", "size"]

@admin.register(OneSTire)
class OneSTireAdmin(ImportMixin,admin.ModelAdmin):
    resource_class = OneSTireResource


@admin.register(Size)
class SizeAdmin(CustomModelAdmin):
    pass
    
