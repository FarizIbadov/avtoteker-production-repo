from django import template
from adv.models import EDVLogo,EDVPercentage

register = template.Library()


@register.simple_tag(name='get_edv')
def get_edv():
    return EDV()


@register.filter(name="get_edv_price")
def get_edv_price(value,percentage):
    price = float(value.sale if value.sale != None else value.price)
    a = price / percentage.get_first_perc()
    edv_price = (price - a) * percentage.get_second_perc()
    return round(edv_price,2)


class EDV:
    def __init__(self):
        logo = EDVLogo.objects.filter(active=True).first()
        percentage = EDVPercentage.objects.filter(active=True).first()
        self.logo = getattr(logo,'get_url',None)
        self.percentage = percentage

        