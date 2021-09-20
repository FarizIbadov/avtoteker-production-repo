from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin

@admin.register(models.NavigationLink)
class NavigationLinkAdmin(TranslationAdmin):
    list_display = ('title','link')
    ordering = ('order_number',)

@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('get_name','active')