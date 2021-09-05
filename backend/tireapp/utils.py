from django import forms
from django.utils.html import escape
from .models import Tire
from .templatetags.url_tags import url_encoder


class CleanedData:
    def get_data(self, key):
        data = self.cleaned_data.get(key)
        if isinstance(data, str):
            return escape(data)
        return data


class OrderedByField(object):
    """
    This mixin just giving ordering fields
    """

    FILTER_BY_FIELDS = {
        "id": "id",
        "brand": "brand__title",
        "serie": "serie__title",
        "size": "size__width size__height size__radius ZR",
        "price": "USDNO",
        "sale": "USD",
        "quantity": "quantity",
    }

    def get_order_by_field(self):
        order = self.request.GET.get("order", "id")
        order_by = self.FILTER_BY_FIELDS[order].split(" ")
        return order_by


class FilterByField(object):
    FILTER_BY_FIELDS = {
        "id": "id",
        "brand": "brand__title",
        "serie": "serie__title",
        "size": "size__width size__height size__radius ZR",
        "price": "USDNO",
        "sale": "USD",
        "quantity": "quantity",
    }

    def filter(self):
        # for field in Tire._meta.get_fields():
        #     if field.is_relation:
        #         # for f in field._meta.get_fields():
        #         #     pass
        #         
        #     else:
        #         pass
        kwargs = {}

        return kwargs


class TableFieldsMixin:
    def get_fields(self):
        columns = {
            "column_1": self.request.GET.get("column_1"),
            "column_2": self.request.GET.get("column_2"),
            "column_3": self.request.GET.get("column_3"),
            "column_4": self.request.GET.get("column_4"),
            "column_5": self.request.GET.get("column_5"),
            "column_6": self.request.GET.get("column_6"),
        }
        return columns


class TireTable:
    def __init__(self, request, tire_list, fields):
        self.request = request
        self.tire_list = tire_list
        self.fields = fields
        self.body = tire_list
        self.header = [
            self.build_header_field("brand"),
            self.build_header_field("serie"),
            self.build_header_field("size", css_class="hidden-at-mobile"),
            self.build_header_field("price"),
            self.build_header_field("sale", css_class="hidden-at-mobile"),
            self.build_header_field("quantity", css_class="hidden-at-mobile"),
        ]

    def build_headers(self):
        pass

    def build_body(self):
        pass

    def build_header_field(self, field, css_class=""):
        return (
            "<th scope='col' class=%s><a class='tireapp__table-head-col-link' href=%s>%s</a></th>"
            % (css_class, url_encoder(self.request, order=field), field.capitalize())
        )
