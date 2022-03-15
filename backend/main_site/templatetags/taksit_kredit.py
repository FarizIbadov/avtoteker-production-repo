from django import template
from django.utils.translation import gettext as _
from tireapp.models import Tire
from kredit_taksit.models import KreditTaksitImage,KreditTaksitInterval

register = template.Library()

taksit_fields = ["birkart","tamkart","bolkart","albalikart"]
taksit_kredit_fields = ["kredit"]
taksit_kredit_fields.extend(taksit_fields)

@register.simple_tag(name="get_kredit_taksit_interval")
def get_kredit_taksit_interval():
    interval = KreditTaksitInterval.objects.filter(active=True).first()
    if not interval:
        return 1000
    return interval.interval
    

@register.simple_tag(name="get_kredit_takist_dataset")
def get_kredit_takist_dataset(value, request):
    carousel_item_datas = []

    code = request.LANGUAGE_CODE

    for field in taksit_kredit_fields:
        month = getattr(value,field,None)

        if not month:
            continue

        try:
            taksit_fields.index(field) 
            taksit = _('{{month}} ay 0%')
            title = taksit.replace("{{month}}", str(month))
            price_title = "%s_%d" % ("taksit", month)
        except ValueError:
            kredit = _("{{month}} ay 0%")
            title = kredit.replace('{{month}}', str(month))
            price_title = "%s_%d" % ("kredit" ,month)
        
        
        price = getattr(value, price_title, None)

        if not price:
            continue

        kredit_taksit = KreditTaksitImage.objects.filter(name=field).first()
        if not kredit_taksit:
            continue
        
        description = getattr(kredit_taksit, f"description_{code}") or ""

        carousel_item_data = TaksitKreditCarouselItemData(
            kredit_taksit.image, 
            title, 
            price, 
            month, 
            description.replace("{{month}}", str(month))
        )   
        
        carousel_item_datas.append(carousel_item_data)

    return carousel_item_datas


@register.filter(name="special_kredit_3_month_price")
def special_kredit_3_month_price(value:Tire):
    price = float(value.price)
    if value.sale:
        price = float(value.sale)

    if value.price_3:
        price_3 = value.get_price_3()
        price = float(price_3)

    kredit_3_price = value.kredit_3_month_price
    kredit_3_result = (price - (price * float(kredit_3_price)/100)) / 3

    return kredit_3_result

@register.filter(name="special_kredit_6_month_price")
def special_kredit_6_month_price(value:Tire):
    price = float(value.price)
    if value.sale:
        price = float(value.sale)

    if value.price_3:
        price_3 = value.get_price_3()
        price = float(price_3)

    kredit_6_price = value.kredit_6_month_price
    kredit_6_result = (price - (price * float(kredit_6_price)/100)) / 6

    return kredit_6_result

@register.filter(name="get_3_month_price")
def get_3_month_price(value):
    price = float(value.price)
    if value.sale:
        price = float(value.sale)

    if value.price_3:
        price_3 = value.get_price_3()
        price = float(price_3)
        
    initial_price = value.kredit_3_month_price
    return price * float(initial_price)/100


@register.filter(name="get_6_month_price")
def get_6_month_price(value):
    price = float(value.price)
    if value.sale:
        price = float(value.sale)
    if value.price_3:
        price_3 = value.get_price_3()
        price = float(price_3)
    initial_price = value.kredit_6_month_price
    return price * float(initial_price)/100

@register.simple_tag(name="get_total_price")
def get_total_price(month, partial_price, initial_price=0):
    return initial_price + month * partial_price


class TaksitKreditCarouselItemData:
    def __init__(self, image, title, price, month, description):
        self.image = image
        self.title = title
        self.price = price
        self.month = month
        self.description = description

