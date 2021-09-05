from django.contrib import admin
from utils.admin import CustomModelAdmin
from .models import Kredit

@admin.register(Kredit)
class KreditAdmin(CustomModelAdmin):
    pass
