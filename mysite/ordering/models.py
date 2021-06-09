from django.db import models
from tireapp.models import Tire
from oilapp.models import Oil
from django.utils import timezone
import uuid

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

    def __str__(self):
        if self.tire:
            return '%s' % self.tire
        else:
            return self.product_title

    def save(self):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super().save()


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

    def __str__(self):
        if self.oil:
            return '%s' % self.oil
        else:
            return self.product_title

    def save(self):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super().save()