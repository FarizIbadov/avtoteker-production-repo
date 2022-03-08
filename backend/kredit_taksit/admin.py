from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import KreditTaksitImage,KreditTaksitInterval

@admin.register(KreditTaksitImage)
class KreditTaksitImageAdmin(TranslationAdmin):
    list_display = ("name","image")

@admin.register(KreditTaksitInterval)
class KreditTaksitIntervalAdmin(admin.ModelAdmin):
    list_display = ("interval",)
