from django.db import models
from tireapp.models import Tire
from django.utils import timezone

class Order(models.Model):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'Kreditlə'),
        (4,'BirKart / TamKart ilə'),
    ]

    tire = models.ForeignKey(Tire,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True,unique=False)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_CHOICES,default=1) 
    is_purchased = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s %s' % (self.tire.brand,self.tire.serie,self.tire.size)


