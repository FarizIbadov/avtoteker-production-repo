from django import template
from main_site.models import PriceColor

register = template.Library()

@register.simple_tag(name="get_price_color")
def get_price_color(instance):
    color = instance.get_price_3_color()
    price_color = PriceColor.objects.filter(color=color).first()
    return price_color


@register.simple_tag(name="get_taksit")
def get_taksit(instance, price_color, month):
    field_name = "taksit_%d" % (month)

    price = getattr(instance, field_name)

    price_3 = instance.get_price_3()

    if price_3 and price_color and price_color.taksit and month <= price_color.taksit:
        price = float(price_3) / month

    return round(price, 2)

