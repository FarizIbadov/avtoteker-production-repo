from django.contrib import admin
from import_export.admin import ImportExportMixin
from . import models
from .resources import SerieResource
from utils.admin import CustomModelAdmin
from modeltranslation.admin import TranslationAdmin

admin.site.site_header = "Avto Teker Admin"
admin.site.site_title = "Avto Teker Admin"

class SubLogoInline(admin.TabularInline):
    model = models.SubLogo

@admin.register(models.Country)
class CountryAdmin(CustomModelAdmin):
    pass

@admin.register(models.Season)
class SeasonAdmin(CustomModelAdmin):
    pass

@admin.register(models.Brand)
class BrandAdmin(TranslationAdmin, CustomModelAdmin):
    pass

@admin.register(models.Serie)
class SerieAdmin(ImportExportMixin,TranslationAdmin, CustomModelAdmin):
    resource_class = SerieResource
    inlines = [SubLogoInline]

    

