from django import forms
from django.utils.html import escape
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
        kwargs = {}

        return kwargs

def generate_trim_code(code):
    splited_code = code.split(" ")
    trimed_part = list(filter(None, splited_code))
    return "".join(trimed_part)

