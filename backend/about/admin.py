from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(models.About)
class AboutAdmin(TranslationAdmin):
    pass