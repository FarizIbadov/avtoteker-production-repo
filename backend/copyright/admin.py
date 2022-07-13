from django.contrib import admin
from .models import Copyright
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Copyright)
class CopyrightAdmin(TranslationAdmin):
    list_display = ('content','active')