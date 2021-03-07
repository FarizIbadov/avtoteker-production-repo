from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Brand,Fuel,OilType,Serie,Viscosity,Volume,Oil
from .forms import OilForm
from .resources import OilResource

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    pass

@admin.register(OilType)
class OilTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    pass

@admin.register(Viscosity)
class ViscosityAdmin(admin.ModelAdmin):
    pass

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    pass

@admin.register(Oil)
class OilAdmin(ImportExportModelAdmin):
    resource_class = OilResource
    form = OilForm
