from django.contrib import admin
from .models import Order
from django.utils.html import format_html


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['product_title']
    exclude = ['phone','tire','product_title','product_link']


    def phone_number(self,obj:Order):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 
    
    def product(self,obj:Order):
        title = ""
        tire = obj.tire
        if tire:
            title = tire
        if not title:
            title = obj.product_title

        link = "<a href='%s'>%s</a>" % (obj.product_link,title)
        return format_html(link)