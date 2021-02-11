from django.db import models
from tireapp.models import Tire
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

class Order(models.Model):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'Kreditlə'),
        (4,'BirKart / TamKart ilə'),
    ]

    name = models.CharField(max_length=20,null=True,blank=True)
    tire = models.ForeignKey(Tire,on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField(default=1)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    order_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True,null=True)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s' % (self.tire.brand,self.tire.serie,self.tire.size)


    # def clean(self,*args, **kwargs):
    #     regex = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
    #     if not re.search(regex,self.phone):
    #         raise ValidationError('Please enter valid phone number!')
    #     super(Order, self).clean(*args, **kwargs)