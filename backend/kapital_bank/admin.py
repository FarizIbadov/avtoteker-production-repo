from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.KapitalPaymentSecurity)
class KapitalPaymentSecurityAdmin(admin.ModelAdmin):
    pass