from django.contrib import admin
from .models import Favicon

@admin.register(Favicon)
class FaviconAdmin(admin.ModelAdmin):
    pass