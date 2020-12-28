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

@register.simple_tag(name="get_address")
def get_address():
    address = Address.objects.filter(active=True).first()
    return AddressClass(address)



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
        if address:
            self.address = address
        else:
            self.address = ""
