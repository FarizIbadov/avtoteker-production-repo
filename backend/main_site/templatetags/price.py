from django import template

register = template.Library()

class Price:
    def __init__(self, value):
        [cash, cent] = str(value).split(".")
        self.cash = cash
        self.cent = cent

@register.simple_tag(name="split_price")
def split_price(value):
    return Price(value)