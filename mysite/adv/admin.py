from django.contrib import admin
from .models import EDVLogo,EDVPercentage

@admin.register(EDVLogo)
class EDVLogoAdmin(admin.ModelAdmin):
    list_display = ['__str__','active']

@admin.register(EDVPercentage)
class EDVPercentageAdmin(admin.ModelAdmin):
    list_display = ['first_percentage','second_percentage','active']