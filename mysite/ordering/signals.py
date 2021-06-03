from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
from tireapp.models import Tire
from .models import Order,OilOrder

@receiver(post_save, sender=Order)
def order_save(sender, instance:Order, created, **kwargs):
    if created:
        instance.product_title = instance.tire.__str__()
        instance.product_link = reverse('detail',kwargs={'pk':instance.tire.id,"slug": instance.tire.slug})
        instance.save()
    
@receiver(post_save, sender=OilOrder)
def oil_order_save(sender, instance:OilOrder, created, **kwargs):
    if created:
        instance.product_title = instance.oil.__str__()
        instance.product_link = reverse('oil-detail',kwargs={'pk':instance.oil.id})
        instance.save()