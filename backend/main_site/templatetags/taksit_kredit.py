from django import template
from django.utils.translation import gettext as _
from tireapp.models import Tire
from kredit_taksit.models import KreditTaksitImage,KreditTaksitInterval

register = template.Library()

taksit_fields = ["birkart","tamkart","bolkart","albalikart"]
taksit_kredit_fields = ["kredit"]
taksit_kredit_fields.extend(taksit_fields)

@register.simple_tag(name="get_kredit_taksit")
def get_kredit_taksit(value, request, manat):
    carousel_item_datas = []
    for field in taksit_kredit_fields:
        month = getattr(value,field,None)

        if not month:
            continue

        try:
            taksit_fields.index(field)
            title = "taksit"   
        except ValueError:
            title = 'kredit'
        
        price_title = "%s_%d" % (title,month)
        price = getattr(value,price_title,None)

        if not price:
            continue

        try:
            kredit_taksit = KreditTaksitImage.objects.get(name=field)
        except KreditTaksitImage.DoesNotExist:
            continue

        
        code = request.LANGUAGE_CODE
        description = getattr(kredit_taksit, f"description_{code}") or ""

        carousel_item_data = {
            "image": kredit_taksit.image.url,
            "title": title,
            "price": round(price, 2),
            "month": month,
            "description": description.replace("{{month}}", str(month))
        }

        carousel_item_datas.append(carousel_item_data)

    return get_template(carousel_item_datas, manat)

def get_template(items, manat):
    carousel_container = """
        <div id="carouselExampleSlidesOnly" class="carousel slide taksit-kredit-container my-2" data-ride="carousel">
            <div class="carousel-inner h-100 kredit-taksit-item ">
                %s        
            </div>
        </div> 
    """

    carousel_item = """
        <div class="carousel-item %s h-100 w-100" data-interval="%s" title="%s">
            <div class="d-flex align-items-center  h-100 w-100">
                <figure class="kredit-taksit-fig mr-2 d-flex h-100" >
                    <img src="%s">
                </figure>
                <div class="flex-fill d-flex bg-light-2 justify-content-center  align-items-center kredit-taksit-carousel-info">
                    <div class="text-center">%s</div>
                    <div class="px-1">%s</div>
                    <div class="text-center">%s</div>
                    <div class="manat">
                        <img src="%s" class="w-100" alt="₼">
                    </div>
                </div>
            </div>
        </div>
    """

    item_templates = []
    interval = str(
        KreditTaksitInterval.objects.filter(active=True).first() or 1000
    )

    seperator = _("|")


    for i in range(len(items)):
        active = "active" if i == 0 else ""
        item = items[i]
        title = ""
        if item['title'] == 'taksit':
            taksit = _('{{month}} ay 0%')
            title = taksit.replace("{{month}}", str(item['month']))
        elif item['title'] == 'kredit':
            kredit = _("{{month}} ay 0%")
            title = kredit.replace('{{month}}', str(item['month']))
        price = f"<span class='text-danger'>{_('ayda')} {item['price']} </span>"
        item_template = carousel_item % (active,interval,item["description"],item['image'],title,seperator, price, manat)
        item_templates.append(item_template)

    return carousel_container % "".join(item_templates) if item_templates else ""


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
    