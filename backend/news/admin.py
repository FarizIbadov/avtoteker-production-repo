from django.contrib import admin
from .models import News
from modeltranslation.admin import TranslationAdmin

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    pass