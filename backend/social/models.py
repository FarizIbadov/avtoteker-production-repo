from django.db import models

class Phone(models.Model):
    number = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class SocialMedia(models.Model):
    CHOICE = [
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('youtube','youtube'),
    ]
    name = models.CharField(choices=CHOICE,max_length=30)
    href = models.URLField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Address(models.Model):
    address = models.CharField(max_length=40)
    longitude = models.FloatField(default=49.877367169701486)
    latidude = models.FloatField(default=40.40432361546929)
    active = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    order_number = models.IntegerField(default=0)
    description = models.TextField(max_length=300,blank=True)
    image = models.ImageField(upload_to="map",blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Addresses"