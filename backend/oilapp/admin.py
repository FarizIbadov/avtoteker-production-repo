from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Brand,Serie,Oil
from .resources import OilResource
from .forms import OilForm
from utils.admin import CustomModelAdmin

from modeltranslation.admin import TranslationAdmin


@admin.register(Brand)
class BrandAdmin(TranslationAdmin,CustomModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(TranslationAdmin,CustomModelAdmin):
    pass

@admin.register(Oil)
class OilAdmin(ImportExportMixin,TranslationAdmin,CustomModelAdmin):
    resource_class = OilResource
    form_class = OilForm


