from django.contrib import admin
from .models import Order,OilOrder
from django.utils.html import format_html


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['phone','tire','product_title','product_link','order_title']


    def phone_number(self,obj:Order):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 
    
    def product(self,obj:Order):
        title = self.order_title(obj)

        link = "<a href='%s'>%s</a>" % (obj.product_link,title)
        return format_html(link)

    def order_title(self,obj:Order):
        title = ""
        tire = obj.tire
        if tire:
            title = tire.__str__()
        else:
            title = obj.product_title

        return title

@admin.register(OilOrder)
class OilOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['phone','oil','product_title','product_link','order_title']


    def phone_number(self,obj:OilOrder):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 
    
    def product(self,obj:OilOrder):
        title = self.order_title(obj)

        link = "<a href='%s'>%s</a>" % (obj.product_link,title)
        return format_html(link)

    def order_title(self,obj:OilOrder):
        title = ""
        oil = obj.oil
        if oil:
            title = oil.__str__()
        else:
            title = obj.product_title

        return title