from django.contrib import admin
from .models import Meta
from .forms import MetaForm


# Register your models here.
@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    form = MetaForm