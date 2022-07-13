from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.PriceColor)
class PriceColorAdmin(admin.ModelAdmin):
    list_display = ('color', "taksit", "kredit")

@admin.register(models.ManatIcon)
class ManatIconAdmin(admin.ModelAdmin):
    pass