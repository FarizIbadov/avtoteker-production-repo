from django.urls import reverse
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.template.loader import render_to_string

from tireapp.models import Tire
from emailapp.models import AuthUser,Email
from .models import Order,OilOrder


@receiver(post_save, sender=Order)
def order_save(sender, instance, created, **kwargs):
    if created:
        instance.product_title = instance.tire.__str__()
        instance.product_link = reverse('detail',kwargs={'pk':instance.tire.id,"slug": instance.tire.slug})

        auth_user = AuthUser.objects.filter(active=True).first()
        if auth_user:
            recipient_list = Email.objects.all().values_list("email",flat=True)
            kwargs = {
                "fail_silently": not settings.DEBUG,
                "subject": "Order",
                "message": "",
                "auth_user": auth_user.email,
                "auth_password": auth_user.password,
                "from_email": auth_user.email,
                "recipient_list": list(recipient_list),
                "html_message": render_to_string('order-email-detail.html',{"object":instance})
            }
            send_mail(**kwargs)

        instance.save()
    
@receiver(post_save, sender=OilOrder)
def oil_order_save(sender, instance, created, **kwargs):
    if created:
        instance.product_title = instance.oil.__str__()
        instance.product_link = reverse('oil-detail',kwargs={'pk':instance.oil.id})

        auth_user = AuthUser.objects.filter(active=True).first()
        if auth_user:
            recipient_list = Email.objects.all().values_list("email",flat=True)
            kwargs = {
                "fail_silently": not settings.DEBUG,
                "subject": "Order",
                "message": "",
                "auth_user": auth_user.email,
                "auth_password": auth_user.password,
                "from_email": auth_user.email,
                "recipient_list": list(recipient_list),
                "html_message": render_to_string('order-email-detail.html',{"object":instance})
            }
            send_mail(**kwargs)
            
        instance.save()