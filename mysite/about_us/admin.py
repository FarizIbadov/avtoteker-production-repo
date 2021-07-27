from django.contrib import admin
from .models import MainContent, SubContent

class SubContentInline(admin.StackedInline):
    model = SubContent
    extra = 1


@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    inlines = [SubContentInline]
