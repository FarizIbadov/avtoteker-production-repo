from django.contrib import admin

from main_site.models import TireListMessage 

# Register your models here.
@admin.register(TireListMessage)
class TireListMessageAdmin(admin.ModelAdmin):
    list_display = ('text','active')