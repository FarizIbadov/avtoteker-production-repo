from django.template.response import TemplateResponse
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from .models import WarrantyTalon, CarType, PDF, CarTire, CarInfo, Payment
from .forms import WarrantyTireSearchForm
from tireapp.models import Tire

import re
import random

class PDFInline(admin.TabularInline):
    model = PDF
    extra = 1 

class CarInfoInline(admin.StackedInline):
    model = CarInfo

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class CarTireInline(admin.StackedInline):
    model = CarTire
    exclude = ('tire',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(WarrantyTalon)
class WarrantyTalonAdmin(admin.ModelAdmin):
    inlines = [PDFInline, CarInfoInline, CarTireInline]
    change_list_template = "admin/warranty/change_list.html"
    change_form_template = "admin/warranty/change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name

        my_urls = [
            path('choose-tire/',
                 self.admin_site.admin_view(self.choose_tire),
                 name='%s_%s_choose-tire' % info),
        ]

        return my_urls + urls

    def choose_tire(self, request, *args, **kwargs):
        form = WarrantyTireSearchForm(request.GET) 
        data = form.data
        query_kwargs = {}

        if data:
            if data.get('code'):
                query_kwargs['code__icontains'] = data['code']
            if data.get('brand'):
                query_kwargs['brand__title__icontains'] = data['brand']
            if data.get('size'):
                size_splitter = re.compile(r"/|\\|-")
                size = "".join(size_splitter.split(data['size']))
                query_kwargs['size__size_code__icontains'] = size
        
        context = {}
        context.update(self.admin_site.each_context(request))
        context['title'] = "Tire Search Warranty"
        context['opts'] = self.model._meta
        context['results'] = Tire.objects.available(**query_kwargs)
        context['payments'] = Payment.objects.filter(child_of=None)
        context['form'] = form
        request.current_app = self.admin_site.name

        return TemplateResponse(request, "admin/warranty/warranty-tire-search.html", context)

    def add_view(self, request, form_url='', extra_context=None):
        object_id = None
        if request.method == 'GET':
            info = self.model._meta.app_label, self.model._meta.model_name

            payment_pk = request.GET.get('payment-1') or request.GET.get('payment-2') or request.GET.get('payment-3') or request.GET.get('payment-4')

            if not request.GET.get('tire') and not payment_pk:
                return redirect('../choose-tire/')

            payment = Payment.objects.filter(pk=payment_pk).first()

            pk = request.GET.get('tire')
            tire = Tire.objects.available(pk=pk).first()

            if not tire:
                return redirect('../choose-tire/')

            warranty_talon = WarrantyTalon.objects.create()
            car_tire = CarTire.objects.create(tire=tire,warranty_talon=warranty_talon, payment=payment)
            car_info = CarInfo.objects.create(warranty_talon=warranty_talon)
            object_id = str(warranty_talon.pk)
        else:
            object_id = request.POST.get("oid")
           
    
        return super().changeform_view(
            request, 
            object_id,
            form_url, 
            {
                "object_id": object_id
            }
        )

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


