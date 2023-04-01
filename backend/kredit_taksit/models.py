from django.db import models

class KreditTaksitImage(models.Model):
    NAME_FIELD = [
        ("birkart","Birkart"),
        ("tamkart","Tamkart"),
        ("bolkart","Bolkart"),
        ("albalikart","Albalikart"),
        ("kredit","Kredit"),
    ]

    image = models.ImageField(upload_to="taksit-kredit", blank=True, null=True)
    name = models.CharField(max_length=20,choices=NAME_FIELD,unique=True)

    description = models.TextField(default="Qeyd olunan şinləri nağd endirimli qiymətlərdən {{month}} ayadək faizsiz, ilkin ödənişsiz və komissiyasız əldə edə bilərsiniz")

    def __str__(self):
        return self.name

class KreditTaksitInterval(models.Model):
    interval = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.interval)