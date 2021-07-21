from django import template
from tireapp.models import Tire
from kredit_taksit.models import KreditTaksitImage,KreditTaksitInterval

register = template.Library()

taksit_fields = ["birkart","tamkart","bolkart","albalikart"]
taksit_kredit_fields = ["kredit"]
taksit_kredit_fields.extend(taksit_fields)

@register.filter(name="get_kredit_taksit")
def get_kredit_taksit(value):
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

        carousel_item_data = {
            "image": kredit_taksit.image.url,
            "title": title,
            "price": price,
            "month": month
        }

        carousel_item_datas.append(carousel_item_data)

    return get_template(carousel_item_datas)

def get_template(items):
    carousel_container = """
        <div id="carouselExampleSlidesOnly" class="carousel slide taksit-kredit-container my-2" data-ride="carousel">
            <div class="carousel-inner h-100 kredit-taksit-item ">
                %s        
            </div>
        </div> 
    """

    carousel_item = """
        <div class="carousel-item %s h-100 w-100" data-interval="%s">
            <div class="d-flex align-items-center  h-100 w-100">
                <figure class="kredit-taksit-fig mr-2 d-flex h-100" >
                    <img src="%s">
                </figure>
                <div class="flex-fill d-flex flex-column justify-content-center h-100">
                    <div class="bg-my-primary text-center">%s</div>
                    <div class="text-center">%s</div>
                </div>
            </div>
        </div>
    """

    item_templates = []
    interval = str(
        KreditTaksitInterval.objects.filter(active=True).first() or 1000
    )


    for i in range(len(items)):
        active = "active" if i == 0 else ""
        title = ""
        item = items[i]
        if item['title'] = 'taksit':
            title = f"{item['month']} {item['title']} 0%"
        elif item['title'] = 'kredit':
            title = f"{item['month']} ay kreditlə"
        price = f"ayda <span class='text-danger'>{item['price']} azn</span>"
        item_template = carousel_item % (active,interval,item['image'],title,price)
        item_templates.append(item_template)

    return carousel_container % "".join(item_templates) if item_templates else ""


@register.filter(name="special_kredit_price")
def special_kredit_price(value:Tire):
    price = float(value.price)
    if value.sale_active:
        price = float(value.sale)

    initial_price = value.kredit_initial_price
    result = (price - (price * float(initial_price)/100)) / 3

    return result

@register.filter(name="get_first_price")
def get_first_price(value):
    price = float(value.price)
    if value.sale_active:
        price = float(value.sale)
    initial_price = value.kredit_initial_price
    return price * float(initial_price)/100
    