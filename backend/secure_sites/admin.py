from django.contrib import admin
from .models import SecureSite

@admin.register(SecureSite)
class SecureSiteAdmin(admin.ModelAdmin):
    pass
