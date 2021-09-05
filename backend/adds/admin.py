from django.contrib import admin
from .models import Add

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ["name",'image','active','duration']
