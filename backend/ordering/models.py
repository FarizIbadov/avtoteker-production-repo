from django.db import models
from django.utils.translation import gettext as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.urls import reverse

from tireapp.models import Tire
from oilapp.models import Oil
from secure_sites.models import SecureSite

from . import managers

import re
import uuid
import phonenumbers

# def coupon_validator(value):
#     if len(value) != 10:
#         raise ValidationError("Coupon code should contain 10 characters")

# class Coupon(models.Model):
#     code = models.CharField(max_length=10,validators=[coupon_validator])
#     discount = models.FloatField(null=True)

#     is_used = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s - %s%%" % (self.code, self.get_dicount())

#     def get_dicount(self):
#         return str(self.discount)

# class CartOrder(models.Model):
#     order_code = models.CharField(max_length=50, null=True)
#     coupon = models.OneToOneField(Coupon, on_delete=models.SET_NULL, null=True, related_name="order_coupon")

#     payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, related_name="order_product")

#     name = models.CharField(max_length=60, null=True)
#     phone = models.CharField(max_length=30, validators=[PhoneValidator()], null=True)
#     email = models.EmailField(blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True)

#     note = models.TextField(blank=True)

#     total_price = models.FloatField(null=True)

#     objects = OrderManager()

#     def get_current_price(self):
#         if self.coupon:
#             current_price = self.total_price - self.total_price * (self.coupon.discount / 100)
#             return str(round(current_price, 2)) + " AZN"
#         return self.total_price
#     get_current_price.short_description = "Current price"

#     def get_total_price(self):
#         return str(self.total_price) + " AZN"
#     get_total_price.short_description = "Total price"

#     def get_phone_number(self):
#         return mark_safe("""
#             <a class="text-underline" href="tel:%s">%s</a>
#         """ % (self.phone, self.phone))
#     get_phone_number.short_description = "Phone number"

#     def save(self, **kwargs):
#         if not self.order_code:
#             self.order_code = str(uuid.uuid4())[:6] + self.generate_phone_code()
#         super().save(**kwargs)


# class Cart(models.Model):
#     user_key = models.CharField(max_length=255,unique=True)
#     total_price = models.FloatField(default=0)

#     objects = managers.CartManager()

#     @property
#     def quantity(self):
#         quantity_list = self.cart_items.values_list('quantity',flat=True)
#         return sum(quantity_list)

#     def update_total_price(self):
#         self.total_price = 0
#         for item in self.cart_items.all():
#             self.total_price += item.get_price()
#         super().save()
#         return self.total_price

#     def __str__(self):
#         return "Cart - %s" % self.user_key


# class CartItem(models.Model):
#     # order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, related_name="order_items", null=True)
#     cart = models.ForeignKey(
#         Cart,
#         on_delete=models.CASCADE,
#         related_name="cart_items",
#         null=True
#     )

#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     product = GenericForeignKey('content_type', 'object_id')

#     quantity = models.PositiveIntegerField()


#     def __str__(self):
#         return self.product.title

#     def increment(self, quantity):
#         self.quantity += quantity
#         super().save()

#     def decrement(self):
#         self.quantity -= 1
#         super().save()



class Order(models.Model):
    PAYMENT_CHOICES = [
        (1,_('Nağd')),
        (2,_('Kart ilə')),
        (3,_('Kreditlə')),
        (4,_('BirKart / TamKart ilə')),
    ]

    TAKSIT_CHOICES = [
        (0, _("---")),
        (2, _("2 ay")),
        (3, _("3 ay")),
        (6, _("6 ay")),
        (9, _("9 ay")),
        (12, _("12 ay"))
    ]

    uuid = models.UUIDField(blank=True,null=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    tire = models.ForeignKey(Tire,on_delete=models.CASCADE,null=True)
    product_title = models.CharField(blank=True,max_length=255)
    product_link = models.CharField(blank=True,max_length=255)
    quantity = models.PositiveSmallIntegerField(default=1)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    taksit_choice = models.PositiveSmallIntegerField(choices=TAKSIT_CHOICES, blank=True, null=True) 
    order_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True,null=True)
    remember_me = models.BooleanField(default=False)
    order_id = models.CharField(blank=True,max_length=255)

    is_purchased = models.BooleanField(default=False)

    lang_code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        if self.tire:
            return '%s' % self.tire
        else:
            return self.product_title

    def save(self, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()

        if not self.order_id:
            id = str(self.tire.pk) 
            phone_number = phonenumbers.parse(self.phone,region="AZ")
            phone = str(phone_number.national_number)[-4:]
            self.order_id = 'T' + id + phone

        super().save(**kwargs)
    
    def get_payment_type(self):
        index = self.payment_type - 1
        return self.PAYMENT_CHOICES[index][1]


    def get_payment_for_email(self):
        if self.payment_type == 4:
            return f"BirKartla ({self.taksit_choice} ay)"

        return self.get_payment_type()


    def get_absolute_product_link(self):
        secure_site = SecureSite.objects.filter(active=True).first()

        if secure_site:
            return secure_site.get_address() + self.product_link

        return self.product_link

    def get_absolute_email_url(self):
        secure_site = SecureSite.objects.filter(active=True).first()
        if secure_site:
            address = secure_site.get_address() + self.tire.get_absolute_url()
        else:
            address = self.tire.get_absolute_url()
        return address

    def get_absolute_payment_url(self):
        secure_site = SecureSite.objects.filter(active=True).first()        
        address = secure_site.get_address() if secure_site else ""

        uuid = self.uuid

        return address + reverse("payment-view", kwargs={
            "uuid": uuid
        })

    def get_total_price(self):
        return self.quantity * self.tire.get_price()

    def get_lang_code(self):
        return self.lang_code if self.lang_code != 'tr' else "az"

    def get_description(self):

        if self.payment_type == 4:
            return f"TAKSIT={self.taksit_choice}"

        return self.get_product_name()
        

    def get_product_name(self):
        qtn_text = _('eded')
        price_text = _("azn")
        return str(self.tire) + f" - {self.quantity} {qtn_text} * {self.tire.get_price()} {price_text} = {self.get_total_price()}"


class OilOrder(models.Model):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'BirKart / TamKart ilə'),
    ]

    uuid = models.UUIDField(blank=True,null=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    oil = models.ForeignKey(Oil,on_delete=models.CASCADE,null=True)
    product_title = models.CharField(blank=True,max_length=255)
    product_link = models.CharField(blank=True,max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    order_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True,null=True)
    remember_me = models.BooleanField(default=False)
    order_id = models.CharField(blank=True,max_length=255)

    def __str__(self):
        if self.oil:
            return '%s' % self.oil
        else:
            return self.product_title        

    def save(self, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        
        if not self.order_id:
            id = str(self.oil.pk) 
            phone_number = phonenumbers.parse(self.phone,region="AZ")
            phone = str(phone_number.national_number)[-4:]
            self.order_id = 'Y' + id + phone

        super().save(**kwargs)

    def get_payment_type(self):
        index = self.payment_type - 1
        return self.PAYMENT_CHOICES[index][1]

    def get_absolute_email_url(self):
        secure_site = SecureSite.objects.filter(active=True).first()
        if secure_site:
            address = secure_site.get_address() + self.oil.get_absolute_url()
        else:
            address = self.tire.get_absolute_url()
        return address


class Result(models.Model):
    CHOICES = [
        ('t','Tire'),
        ('o','Oil')
    ]

    head = models.CharField(max_length=100)
    sub = models.TextField()
    message = models.CharField(max_length=200,default="Oldı, təşəkür edirik")
    order_id_part = models.CharField(max_length=100)
    order_type = models.CharField(max_length=1,choices=CHOICES)
    active = models.BooleanField(default=True)

    def __str__(self): 
        return self.head

