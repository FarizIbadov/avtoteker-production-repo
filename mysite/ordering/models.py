from django.db import models
from tireapp.models import Tire
from oilapp.models import Oil
from django.utils import timezone
import uuid
import phonenumbers

import re

class Order(models.Model):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'Kreditlə'),
        (4,'BirKart / TamKart ilə'),
    ]

    uuid = models.UUIDField(blank=True,null=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    tire = models.ForeignKey(Tire,on_delete=models.CASCADE,null=True)
    product_title = models.CharField(blank=True,max_length=50)
    product_link = models.CharField(blank=True,max_length=150)
    quantity = models.PositiveSmallIntegerField(default=1)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    order_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True,null=True)
    remember_me = models.BooleanField(default=False)
    order_id = models.CharField(blank=True,max_length=20)

    def __str__(self):
        if self.tire:
            return '%s' % self.tire
        else:
            return self.product_title

    def save(self,force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.uuid:
            self.uuid = uuid.uuid4()

        if not self.order_id:
            id = str(self.tire.pk) 
            phone_number = phonenumbers.parse(self.phone,region="AZ")
            phone = str(phone_number.national_number)[-4:]
            self.order_id = 'T' + id + phone

        super().save(force_insert, force_update, using,
             update_fields)


class OilOrder(models.Model):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'BirKart / TamKart ilə'),
    ]

    uuid = models.UUIDField(blank=True,null=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    oil = models.ForeignKey(Oil,on_delete=models.CASCADE,null=True)
    product_title = models.CharField(blank=True,max_length=50)
    product_link = models.CharField(blank=True,max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    order_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True,null=True)
    remember_me = models.BooleanField(default=False)
    order_id = models.CharField(blank=True,max_length=20)

    def __str__(self):
        if self.oil:
            return '%s' % self.oil
        else:
            return self.product_title        

    def save(self,force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        
        if not self.order_id:
            id = str(self.oil.pk) 
            phone_number = phonenumbers.parse(self.phone,region="AZ")
            phone = str(phone_number.national_number)[-4:]
            self.order_id = 'Y' + id + phone

        super().save(force_insert, force_update, using,
             update_fields)

class Result(models.Model):
    CHOICES = [
        ('t','Tire'),
        ('o','Oil')
    ]

    head = models.CharField(max_length=100)
    sub = models.TextField()
    order_id_part = models.CharField(max_length=100)
    order_type = models.CharField(max_length=1,choices=CHOICES)
    active = models.BooleanField(default=True)

    def __str__(self): 
        return self.head