from django.contrib import admin
from .models import KreditTaksitImage

@admin.register(KreditTaksitImage)
class KreditTaksitImageAdmin(admin.ModelAdmin):
    list_display = ("name","image")
