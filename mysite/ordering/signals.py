from django.template.loader import get_template
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from tireapp.models import Tire
from .models import Order

from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from django.contrib.staticfiles import finders

import os

@receiver(post_save, sender=Order)
def order_save(sender, instance:Order, created, **kwargs):
    if created:
        instance.note = instance.tire
    