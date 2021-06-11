from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Post

@admin.register(Post)
class PostAdmin(ImportExportMixin,admin.ModelAdmin):
    pass