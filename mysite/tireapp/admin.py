from django.contrib import admin
from .forms import TireForm
from .models import Tire,Size,DefaultImage
from import_export.admin import ImportExportModelAdmin
from .resources import TireResource


@admin.register(Tire)
class TireAdmin(ImportExportModelAdmin):
    form = TireForm
    resource_class = TireResource
    list_display = ["brand", "serie", "size", "manufacturer"]
    list_filter = ["brand", "serie", "manufacturer", "size"]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
    

@admin.register(DefaultImage)
class DefaultImageAdmin(admin.ModelAdmin):
    pass