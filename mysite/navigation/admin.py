from django.contrib import admin
from . import models

@admin.register(models.NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('title','link')
    ordering = ('order_number',)

@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('get_name','active')