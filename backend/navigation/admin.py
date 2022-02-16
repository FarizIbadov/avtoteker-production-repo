from django.contrib import admin
from . import models, forms
from modeltranslation.admin import TranslationAdmin


@admin.register(models.UrlName)
class UrlNameAdmin(admin.ModelAdmin):
    form = forms.UrlNameForm
    list_display = ('title', "link")

# @admin.register(models.NavigationLink)
# class NavigationLinkAdmin(TranslationAdmin):
#     list_display = ('title', "link")
#     ordering = ('order_number',)

@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('get_name','active')