from django import template
from tireapp.models import Tire

register = template.Library()

@register.filter(name="get_taksit")
def get_taksit(value):
    active_taksits = []
    for field in taksit_fields:
        field_data = get_field_data(field,value)
        if field_data[0]:
            active_taksits.append(field_data[1])
    if len(active_taksits) == 0:
        return ""
    last_taksit = active_taksits[-1]
    return get_kredit_taksit_template(last_taksit,'taksit')

@register.filter(name="get_kredit")
def get_kredit(value):
    active_kredits = []
    for field in kredit_fields:
        field_data = get_field_data(field,value)
        if field_data[0]:
            active_kredits.append(field_data[1])
    if len(active_kredits) == 0:
        return "" 
    last_kredit = active_kredits[-1]
    return get_kredit_taksit_template(last_kredit,'kredit')

def get_field_data(field,value):
    field_active = field + "_active"
    field_month = field + "_month"
    return (getattr(value,field_active),{
        "value": getattr(value,field),
        "month":getattr(value,field_month)
    })

def get_kredit_taksit_template(value,word):
    first_part = """
        <div class="price text-right">
            <span class="text-red">ayda %s</span>
        </div>  
    """ % (value['value'])
    second_part = """
        <div class="text-right">
            %s %s
        </div>
    """ % (value['month'],word)
    return "".join([first_part,second_part])

kredit_fields = ["kredit_3","kredit_6","kredit_9","kredit_12"]
taksit_fields = ["taksit_2","taksit_3","taksit_6","taksit_9","taksit_12"]

"""
<div class="price text-right">
    <span class="text-red">ayda %s</span>
    <span class="manat">₼</span>
</div>  
<div class="text-right">
    %s %s
</div>
"""

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