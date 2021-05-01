from django.contrib import admin
from .models import NavigationLink
from utils.admin import CustomModelAdmin

@admin.register(NavigationLink)
class NavigationLinkAdmin(CustomModelAdmin):
    list_display = ('title','link')
    ordering = ('deleted','order_number')