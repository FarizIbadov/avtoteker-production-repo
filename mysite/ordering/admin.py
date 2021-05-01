from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Order,OilOrder
from django.utils.html import format_html
from .resources import OilOrderResource,TireOrderResource


@admin.register(Order)
class OrderAdmin(ExportMixin,admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['phone','tire','product_title','product_link','order_title']

    resource_class = TireOrderResource

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
class OilOrderAdmin(ExportMixin,admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['phone','oil','product_title','product_link','order_title']

    resource_class = OilOrderResource


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