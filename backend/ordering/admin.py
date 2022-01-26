from django.contrib import admin
from import_export.admin import ExportMixin
from . import models
from django.utils.html import format_html
from .resources import OilOrderResource,TireOrderResource


@admin.register(models.Order)
class OrderAdmin(ExportMixin, admin.ModelAdmin):
    readonly_fields = ['customer_id','product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['uuid','phone','tire','product_title','product_link','order_title', "lang_code"]
    search_fields = ("uuid",)

    resource_class = TireOrderResource

    change_form_template = "admin/order/order.html"
    

    def phone_number(self,obj):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 

    def customer_id(self,obj):
        return obj.uuid if obj.uuid else "-" 
    
    def product(self,obj):
        title = self.order_title(obj)

        link = "<a href='%s'>%s</a>" % (obj.product_link,title)
        return format_html(link)

    def order_title(self,obj):
        title = ""
        tire = obj.tire
        if tire:
            title = tire.__str__()
        else:
            title = obj.product_title

        return title

@admin.register(models.OilOrder)
class OilOrderAdmin(ExportMixin,admin.ModelAdmin):
    readonly_fields = ['product','email','phone_number','payment_type','name']
    list_filter = ['remember_me']
    list_display = ['order_title']
    exclude = ['phone','oil','product_title','product_link','order_title']

    resource_class = OilOrderResource


    def phone_number(self,obj):
        link = "<a href='tel:%s'>%s</a>" % (obj.phone,obj.phone)
        return format_html(link) 

    def customer_id(self,obj):
        return obj.uuid if obj.uuid else "-" 
    
    def product(self,obj):
        title = self.order_title(obj)

        link = "<a href='%s'>%s</a>" % (obj.product_link,title)
        return format_html(link)

    def order_title(self,obj):
        title = ""
        oil = obj.oil
        if oil:
            title = oil.__str__()
        else:
            title = obj.product_title

        return title

@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("head",'order_type')