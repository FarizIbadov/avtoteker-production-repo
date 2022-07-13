from django.db import models
from django.core.validators import ValidationError
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


class Order(models.Model):
    PAYMENT_CHOICES = [
        (1, _('Nağd')),
        (2, _('Kart ilə')),
        (3, _('Kreditlə')),
        (4, _('BirKart')),
        (5, _("TamKart"))
    ]

    TAKSIT_CHOICES = [
        (0, _("---")),
        (2, _("2 ay")),
        (3, _("3 ay")),
        (6, _("6 ay")),
        (9, _("9 ay")),
        (12, _("12 ay"))
    ]

    PRICE_CHOICES = [
        (1, "Price 1"),
        (2, "Price 2"),
        (3, "Price 3"),
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

    change_amount = models.FloatField(default=0, blank=True)

    change_percentage = models.FloatField(default=0, blank=True)
    by_percentage = models.BooleanField(default=False)

    by_price = models.PositiveSmallIntegerField(choices=PRICE_CHOICES, default=2)

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

        self.change_price()

        super().save(**kwargs)

    def get_tire_price(self):
        tire_price = self.tire.get_price()

        if self.by_price == 1:
            tire_price = self.tire.price  
        elif self.by_price == 2 and self.tire.sale:
            tire_price = self.tire.sale 

        return tire_price

    def change_price(self):
        tire_price = self.get_tire_price()
        coef = 1

        if self.by_percentage:
            if self.change_percentage != 0:
                coef = self.change_percentage / abs(self.change_percentage)
            amount = tire_price * (abs(self.change_percentage) / 100)
            self.change_amount = coef * round(amount, 2)
        else:
            if self.change_amount != 0:
                coef = self.change_amount / abs(self.change_amount)
            percentage = (abs(self.change_amount) * 100) / tire_price
            self.change_percentage = coef * round(percentage, 2)

        self.by_percentage = False
        self.by_amount = False

    
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

    def get_single_tire_price(self):
        tire_price = self.tire.get_price()
        return tire_price + ((self.change_percentage / 100) * tire_price)

    def get_total_price(self):
        original_price = self.quantity * self.get_single_tire_price()
        return original_price

    @property
    def tire_price(self):
        tire_price = self.tire.get_price()
        operator = "+"

        single_tire_price = self.get_single_tire_price()

        new_price = round(single_tire_price, 2)

        if self.change_percentage < 0:
            operator = "-"


        return f"{tire_price} AZN {operator} {abs(self.change_percentage)}% = {new_price} AZN\n\n {self.quantity} ed * {new_price} AZN = {round(self.get_total_price(), 2)} AZN"

    # @property
    # def total_price(self):
    #     return f"{}"

    


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

