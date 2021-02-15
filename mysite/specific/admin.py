from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Country, Season, Brand, Serie
from .resources import SerieResource

admin.site.site_header = "Avto Teker Admin"
admin.site.site_title = "Avto Teker Admin"

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(ImportExportModelAdmin):
    resource_class = SerieResource

    

