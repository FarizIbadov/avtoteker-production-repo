from django import template
from social.models import Phone,SocialMedia,Address

register = template.Library()

@register.simple_tag(name="get_social_media")
def get_social_media():
    return SocialMedia.objects.all().filter(active=True)[:3]

@register.simple_tag(name="get_phone")
def get_phone():
    phone_obj = Phone.objects.all().filter(active=True)
    phone = PhoneClass(phone_obj)
    return phone

@register.simple_tag(name="get_addresses")
def get_addresses():
    addresses = Address.objects.filter(active=True).order_by("order_number")
    prepeared_addresses = []

    for address in addresses:
        adr = AddressClass(address)
        prepeared_addresses.append(adr)

    return prepeared_addresses

class PhoneClass:
    def __init__(self,phone):
        if phone:
            self.label = phone[0].number
            splited_number = phone[0].number.split(" ")
            joined_number = ''.join(splited_number)
            self.number = joined_number.replace('0',"tel:+994",1)
        else:
            self.label = ""
            self.number = ""

    def __str__(self):
        return self.label

class AddressClass:
    def __init__(self,address):
        self.address = address.address
        self.lon = address.longitude
        self.lat = address.latidude
        self.extra = "<span class='text-danger font-weight-bold'>(tezliklə)</span>" if address.new else "" 
        self.description = address.description
        self.image = address.image
  
   
