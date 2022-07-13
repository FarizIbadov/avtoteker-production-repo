from django.db import models
from private_storage.fields import PrivateFileField

class KapitalPaymentSecurity(models.Model):
    crt_file = PrivateFileField(upload_to="crt/")
    key_file = PrivateFileField(upload_to="key/")

    merchant_id = models.CharField(
        max_length=255, 
        default="E1000010"
    )  

    service_link = models.CharField(
        max_length=255,
        default="https://e-commerce.kapitalbank.az:5443/Exec"
    )

    payment_link = models.CharField(
        max_length=255,
        default="https://e-commerce.kapitalbank.az/index.jsp?ORDERID={{ORDERID}}&SESSIONID={{SESSIONID}}"
    )

    verify = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    def __str__(self):
        return "Kapital Security"