from django.db import models

class Phone(models.Model):
    number = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class SocialMedia(models.Model):
    name = models.CharField(max_length=30)
    href = models.URLField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Address(models.Model):
    address = models.CharField(max_length=40)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Addresses"