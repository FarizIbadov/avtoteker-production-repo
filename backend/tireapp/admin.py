from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.utils.encoding import force_str
from django.contrib.messages import add_message, ERROR, SUCCESS

from import_export.forms import ImportForm
from import_export.formats.base_formats import XLS, XLSX

from .forms import TireForm
from . import models
from import_export.admin import ImportExportMixin,ImportMixin
from utils.admin import CustomModelAdmin
from .resources import TireResource, OsTireImporter
from modeltranslation.admin import TranslationAdmin


class OsMixin:
    def get_urls(self):
        urls = super().get_urls()
        info = self.get_model_info()

        my_urls = [
            path("os-import/",self.admin_site.admin_view(self.os_import),
                name='%s_%s_os-import' % info)
        ]

        return my_urls + urls

    def os_import(self, request, *args, **kwargs):
        try:
            formats = [XLSX, XLS]
        
            form = ImportForm(
                formats, 
                request.POST or None, 
                request.FILES or None,
                **kwargs
            )

            if request.method == "POST" and form.is_valid():
                input_format = formats[
                    int(form.cleaned_data['input_format'])
                ]()
                import_file = form.cleaned_data['import_file']
                tmp_storage = self.write_to_tmp_storage(import_file, input_format)

                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_str(data, self.from_encoding)

                dataset = input_format.create_dataset(data)
                importer = OsTireImporter(dataset)
                importer.process_import()
                importer.process_save()
                add_message(request, SUCCESS, "File was imported successfully")
        except Exception as e:
            add_message(request,ERROR, e)

        context = {}
        context.update(self.admin_site.each_context(request))
        context['title'] = "Os Tire Importer"
        context['opts'] = self.model._meta
        context['form'] = form
        request.current_app = self.admin_site.name

        return TemplateResponse(request, "admin/os-tire/os-form.html", context)

@admin.register(models.Tire)
class TireAdmin(ImportExportMixin, OsMixin, CustomModelAdmin):
    form = TireForm
    resource_class = TireResource
    search_fields = ("brand__title","serie__title","quantity","manufacturer__title") 
    exclude = ("size", "trim_code")
    list_display = ["brand", "serie", "size", "manufacturer","quantity"]
    list_filter = ["brand", "serie", "manufacturer", "size"]

    change_list_template = "admin/os-tire/change-list-import-export.html"


@admin.register(models.Size)
class SizeAdmin(CustomModelAdmin):
    exclude = ("size_code",)
    
@admin.register(models.OsTireImporterSetting)
class OsTireImporterSettingAdmin(admin.ModelAdmin):
    pass

@admin.register(models.OE)
class OEAdmin(TranslationAdmin):
    pass

@admin.register(models.TireYear)
class TireYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'active')

@admin.register(models.TireClass)
class TireClassAdmin(TranslationAdmin):
    pass
