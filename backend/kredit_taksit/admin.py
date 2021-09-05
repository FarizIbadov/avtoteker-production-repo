from django.contrib import admin
from .models import KreditTaksitImage,KreditTaksitInterval

@admin.register(KreditTaksitImage)
class KreditTaksitImageAdmin(admin.ModelAdmin):
    list_display = ("name","image")

@admin.register(KreditTaksitInterval)
class KreditTaksitIntervalAdmin(admin.ModelAdmin):
    list_display = ("interval",)
