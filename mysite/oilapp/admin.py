from django.contrib import admin

from .models import Brand,Fuel,OilType,Serie,Viscosity,Volume,Oil
from .forms import OilForm

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
class OilAdmin(admin.ModelAdmin):
    form = OilForm
