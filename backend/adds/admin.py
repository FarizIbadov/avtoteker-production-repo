from django.contrib import admin
from .models import Add
from modeltranslation.admin import TranslationAdmin

@admin.register(Add)
class AddAdmin(TranslationAdmin):
    list_display = ["__str__",'image','active','duration']
