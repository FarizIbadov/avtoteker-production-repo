from django.db import models

class Phone(models.Model):
    number = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.number + " " + (self.label if self.label else "")


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
    address = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(null=True)
    latidude = models.FloatField(null=True)
    zoom = models.FloatField(default=17, null=True)
    map_image = models.ImageField(upload_to="map", null=True)
    active = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    order_number = models.IntegerField(default=0)
    description = models.TextField(max_length=300,blank=True)
    image = models.ImageField(upload_to="map",blank=True)

    def __str__(self):
        return self.address

    @property
    def href(self):
        return "https://www.google.com/maps/place/@%f,%f,%fz/" % (self.latidude, self.longitude, self.zoom)

    class Meta:
        verbose_name_plural = "Addresses"