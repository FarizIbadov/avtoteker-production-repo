from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Country, Season, Brand, Serie
from .resources import SerieResource
from utils.admin import CustomModelAdmin

admin.site.site_header = "Avto Teker Admin"
admin.site.site_title = "Avto Teker Admin"

@admin.register(Country)
class CountryAdmin(CustomModelAdmin):
    pass

@admin.register(Season)
class SeasonAdmin(CustomModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(CustomModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(ImportExportMixin,CustomModelAdmin):
    resource_class = SerieResource

    

