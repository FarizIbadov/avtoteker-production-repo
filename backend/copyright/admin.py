from django.contrib import admin
from .models import Copyright

# Register your models here.
@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('content','active')