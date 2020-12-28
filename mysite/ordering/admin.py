from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['tire','email','phone','payment_type']
