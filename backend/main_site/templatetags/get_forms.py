from django import template
from ordering import forms

register = template.Library()

@register.simple_tag(name="get_tire_form")
def get_tire_form():
    return forms.OrderForm

@register.simple_tag(name="get_oil_form")
def get_oil_form():
    return forms.OilOrderForm