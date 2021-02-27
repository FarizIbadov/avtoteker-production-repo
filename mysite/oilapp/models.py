import os
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  
from django.core.exceptions import ValidationError
from specific.models import Country

class Volume(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Fuel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Viscosity(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Viscosities"

class OilType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name="oil_brand"
    )
    logo = models.ImageField(upload_to="oil-brand")
    description = RichTextUploadingField()
    show_in_slider = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Serie(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="oil-serie",blank=True)
    description = RichTextUploadingField()

    def __str__(self):
        return f"{self.title}"

class Oil(models.Model):
    EXTENSIONS = [
        'jpg',
        'png',
        "jpeg"
    ]

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True
    )

    serie = models.ForeignKey(
        Serie,
        on_delete=models.SET_NULL,
        null=True
    )

    volume = models.ForeignKey(
        Volume,
        on_delete=models.SET_NULL,
        null=True
    )

    viscosity = models.ForeignKey(
        Viscosity,
        on_delete=models.SET_NULL,
        null=True,
    )

    fuel = models.ForeignKey(
        Fuel,
        on_delete=models.SET_NULL,
        null=True
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True
    )

    oil_type = models.ForeignKey(
        OilType,
        on_delete=models.SET_NULL,
        null=True
    )

    description = RichTextUploadingField()
    image = models.ImageField(upload_to="oil",blank=True)
    image_url = models.URLField(blank=True)
    des1 = models.CharField(max_length=50)

    price = models.FloatField()
    sale = models.FloatField()
    sale_active = models.BooleanField(default=False)

    taksit_active = models.BooleanField(default=True)

    taksit_2 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    taksit_2_month = models.PositiveSmallIntegerField(default=2)
    taksit_2_active = models.BooleanField(default=True)

    taksit_3 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    taksit_3_month = models.PositiveSmallIntegerField(default=3)
    taksit_3_active = models.BooleanField(default=True)

    taksit_6 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    taksit_6_month = models.PositiveSmallIntegerField(default=6)
    taksit_6_active = models.BooleanField(default=True)

    taksit_9 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    taksit_9_month = models.PositiveSmallIntegerField(default=9)
    taksit_9_active = models.BooleanField(default=True)

    taksit_12 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    taksit_12_month = models.PositiveSmallIntegerField(default=12)
    taksit_12_active = models.BooleanField(default=True)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return self.image_url

    def __str__(self):
        return f"{self.brand.title} - {self.serie.title}"

    def clean(self,*args,**kwargs):
        if self.image or self.image_url:
            if self.image_url:
                file_name = os.path.basename(self.image_url)
                extension = file_name.split(".")[-1]
                
                if not (self.EXTENSIONS.index(extension) >= 0):
                    raise ValidationError("Invalid type")
                
            super(Oil, self).clean(*args, **kwargs)
        else:
            raise ValidationError("Please enter image or image url")