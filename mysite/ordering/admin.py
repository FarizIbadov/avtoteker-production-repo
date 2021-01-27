from django.contrib import admin
from .models import Order
from django.utils.html import format_html


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['tire','email','phone_number','payment_type','name']
    list_filter = ['remember_me']


    def phone_number(self,obj):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 