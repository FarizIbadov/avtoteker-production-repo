from django.db import models

class KreditTaksitImage(models.Model):
    NAME_FIELD = [
        ("birkart","Birkart"),
        ("tamkart","Tamkart"),
        ("bolkart","Bolkart"),
        ("albalikart","Albalikart"),
        ("kredit","Kredit"),
    ]

    image = models.ImageField(upload_to="taksit-kredit")
    name = models.CharField(max_length=20,choices=NAME_FIELD,unique=True)

    def __str__(self):
        return self.name

class KreditTaksitInterval(models.Model):
    interval = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.interval)