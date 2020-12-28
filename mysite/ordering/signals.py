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
def order_save(sender, instance, created, **kwargs):
    if created and instance.email:
        img_url = finders.find(path='img/logo.png',all=False)
        img_data = open(img_url,'rb').read()
        domain = os.environ.get('HOST',"http://localhost:8000")
        context = {'content':"Test",'domain':domain}
        html_content = MIMEMultipart(_subtype='related')
        body = MIMEText(get_template('email.html').render(context),_subtype="html")
        html_content.attach(body)

        img = MIMEImage(img_data,'png')
        img.add_header('Content-Id', '<logoimage>')
        img.add_header("Content-Disposition", "inline", filename="logo.png")
        html_content.attach(img)
        
        email = EmailMultiAlternatives(
            "Payment Bill",
            None,
            settings.EMAIL_HOST_USER,
            [instance.email],
        )
        email.attach(html_content)
        email.send()

    elif not created and instance.is_purchased:
        order_qtn = instance.quantity
        tire = instance.tire
        qtn = tire.quantity - order_qtn
        instance.tire.quantity = qtn
        instance.tire.save()
    