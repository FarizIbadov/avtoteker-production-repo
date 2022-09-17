from django.db import models
from app.utils import compress
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from utils.models import CustomModel

from navigation.models import Logo


class Season(CustomModel):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="season", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url

        logo = Logo.objects.filter(active=True).first()

        if logo:
            return logo.logo.url

        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.optimize_image()

    def optimize_image(self):
        if self.image:
            compress(self.image.path, (480, 480))


class Country(CustomModel):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="country", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url

        logo = Logo.objects.filter(active=True).first()

        if logo:
            return logo.logo.url

        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.optimize_image()

    def optimize_image(self):
        if self.image:
            compress(self.image.path, (480, 480))

    class Meta:
        verbose_name_plural = "Countries"


class Brand(CustomModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brand", blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    one_year_free_service = models.BooleanField(default=False)
    two_year_free_service = models.BooleanField(default=False)

    one_year_warranty = models.BooleanField(default=False)

    order_number = models.IntegerField(default=1)
    description = RichTextUploadingField(blank=True, null=True)
    show_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.optimize_image()

    def optimize_image(self):
        if self.image:
            compress(self.image.path, (480, 480))

    def get_image(self):
        if self.image:
            return self.image.url

        logo = Logo.objects.filter(active=True).first()

        if logo:
            return logo.logo.url

        return self.title

    def get_free_service(self):
        return self.one_year_free_service or self.two_year_free_service


class Serie(CustomModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="serie", blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    dry = models.PositiveSmallIntegerField(default=0)
    wet = models.PositiveSmallIntegerField(default=0)
    offroad = models.PositiveSmallIntegerField(default=0)
    comfort = models.PositiveSmallIntegerField(default=0)
    noise = models.PositiveSmallIntegerField(default=0)
    treadware = models.PositiveSmallIntegerField(default=0)
    snow = models.PositiveSmallIntegerField(default=0)
    value = models.PositiveSmallIntegerField(default=0)
    description = RichTextUploadingField(blank=True, null=True)
    extra = RichTextUploadingField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            compress(self.image.path, quality=90)

    def get_image(self):
        if self.image:
            return self.image.url

        logo = Logo.objects.filter(active=True).first()

        if logo:
            return logo.logo.url

        return self.title


class SubLogo(models.Model):
    logo = models.ImageField(upload_to="sub-logo/", null=True)
    serie = models.ForeignKey(
        Serie, on_delete=models.CASCADE, null=True, related_name="serie_sub_logos")

    order = models.PositiveSmallIntegerField(null=True)

    def get_image(self):
        if self.logo:
            return self.logo.url

        logo = Logo.objects.filter(active=True).first()

        if logo:
            return logo.logo.url

        return "Logo"

    class Meta:
        ordering = ("order",)
