from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from mysite.mixins import IsAdmin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)
from tablib import Dataset
from .forms import ExcelForms, TireForm, PaginateByForm
from .models import Tire
from .utils import OrderedByField, FilterByField, TableFieldsMixin, TireTable
from django.urls import reverse_lazy
from .resources import TireResource


class TireListView(IsAdmin, TableFieldsMixin, FilterByField, OrderedByField, ListView):
    template_name = "tireapp/list.html"

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get("per_page", 100)
        return paginate_by

    def get_queryset(self):
        order_by = self.get_order_by_field()
        kwargs = self.filter()
        return Tire.objects.filter(**kwargs).order_by(*order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tire_list = context["object_list"]
        fields = self.get_fields()
        context["object_list"] = TireTable(self.request, tire_list, fields)
        context["form"] = ExcelForms
        context["page_by_form"] = PaginateByForm
        return context


class TireCreateView(IsAdmin, CreateView):
    form_class = TireForm
    template_name = "tireapp/form.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.updator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.__dict__)
        return super().form_invalid(form)


class TireUpdateView(IsAdmin, UpdateView):
    form_class = TireForm
    model = Tire
    template_name = "tireapp/form.html"

    def form_valid(self, form):
        form.instance.updator = self.request.user
        return super().form_valid(form)


class TireDetailView(IsAdmin, DetailView):
    template_name = "tireapp/detail.html"
    model = Tire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = context["object"].brand
        serie = context["object"].serie
        size = context["object"].get_size()

        context["title"] = f"{brand} - {serie} - {size}"
        return context


class TireDeleteView(IsAdmin, DeleteView):
    model = Tire

    def get_success_url(self):
        return reverse_lazy("custom-admin:tireapp:home")


class TireExcelView(View):
    def get(self, request, *args, **kwargs):
        mime_types = {
            "xls": "application/vnd.ms-excel",
            "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }
        file_format = request.GET.get("file_format")
        mime_type = mime_types.get(file_format, "xls")
        tire_resource = TireResource()
        dataset = tire_resource.export()

        tire_list = getattr(dataset, file_format)

        response = HttpResponse(tire_list, content_type=mime_type)
        response["Content-Disposition"] = 'attachment; filename="tires.%s"' % (
            file_format
        )
        return response

    def post(self, request, *args, **kwargs):
        tire_resource = TireResource()
        excel_form = ExcelForms().imports(data=request.POST, files=request.FILES)
        dataset = Dataset()

        if not excel_form.is_valid():
            messages.error(request, "Provide .xlsx, .xls file!", extra_tags="danger")
        else:
            try:
                new_file = excel_form.cleaned_data.get("_file")
                file_format = new_file._name.split(".")[-1]
                dataset.load(new_file.read(), format=file_format)
                tire_resource.import_data(dataset, dry_run=False,raise_errors=True)
                messages.success(
                    request, "File was imported successfully!", extra_tags="success"
                )
            except Exception:
                messages.error(request, "Invalid content!", extra_tags="danger")

        return redirect("custom-admin:tireapp:home")
