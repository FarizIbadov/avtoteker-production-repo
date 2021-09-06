import os
from django.urls import reverse  
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  
from django.core.exceptions import ValidationError
from specific.models import Country
from utils.models import CustomModel
from mysite.utils import compress

from sticker.models import Sticker
from campaign.models import Post

class Brand(CustomModel):
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

class Serie(CustomModel):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="oil-serie",blank=True)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

class Oil(CustomModel):
    EXTENSIONS = [
        'jpg',
        'png',
        "jpeg"
    ]

    BIRKART_CHOICES = [
        (0,"Yoxdur"),
        (2,"2 ay"),
        (3,"3 ay"),
        (6,"6 ay"),
        (9,"9 ay"),
        (12,"12 ay")
    ]

    TAMKART_CHOICES = [
        (0,"Yoxdur"),
        (2,"2 ay"),
        (3,"3 ay"),
        (6,"6 ay"),
        (9,"9 ay"),
        (12,"12 ay")
    ]

    BOLKART_CHOICES = [
        (0,"Yoxdur"),
        (2,"2 ay"),
        (3,"3 ay"),
        (6,"6 ay"),
        (9,"9 ay"),
        (12,"12 ay")
    ]

    ALBALI_CHOICES = [
        (0,"Yoxdur"),
        (2,"2 ay"),
        (3,"3 ay"),
        (6,"6 ay"),
        (9,"9 ay"),
        (12,"12 ay")
    ]

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=True
    )

    serie = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        null=True
    )

    volume = models.CharField(max_length=20,null=True)
    viscosity = models.CharField(max_length=20,null=True)
    fuel = models.CharField(max_length=50,null=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True
    )

    oil_type = models.CharField(max_length=20,null=True)

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

    taksit_2_active = models.BooleanField(default=True)

    taksit_3 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )

    taksit_3_active = models.BooleanField(default=True)

    taksit_6 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )

    taksit_6_active = models.BooleanField(default=True)

    taksit_9 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    
    taksit_9_active = models.BooleanField(default=True)

    taksit_12 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    
    taksit_12_active = models.BooleanField(default=True)

    birkart = models.PositiveSmallIntegerField(choices=BIRKART_CHOICES,blank=True)
    tamkart = models.PositiveSmallIntegerField(choices=TAMKART_CHOICES,blank=True)
    bolkart = models.PositiveSmallIntegerField(choices=BOLKART_CHOICES,blank=True)
    albalikart = models.PositiveSmallIntegerField(choices=ALBALI_CHOICES,blank=True)

    stickers = models.ManyToManyField(Sticker,related_name='oils',blank=True)
    campaigns = models.ManyToManyField(Post,related_name="oils",blank=True)

    

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url

    def get_absolute_url(self):
        return reverse(
            "oil-detail", kwargs={"pk": self.id}
        )

    def __str__(self):
        return f"{self.brand.title} - {self.serie.title}"

    def save(self):
        if not self.albalikart:
            self.albalikart = self.get_active_price("taksit")
        if not self.tamkart:
            self.tamkart = self.get_active_price("taksit")
        if not self.bolkart:
            self.bolkart = self.get_active_price("taksit")
        if not self.birkart:
            self.birkart = self.get_active_price("taksit")
        super().save()

        # compress(self.image.url,quality=90)

    def get_active_price(self,taksit_kredit_title):
        kredit_list = ['kredit_3','kredit_6','kredit_9','kredit_12']
        taksit_list = ['taksit_2','taksit_3','taksit_6','taksit_9','taksit_12']

        iterable_list = taksit_list
        active_months = [] 

        if taksit_kredit_title == 'kredit':
            iterable_list = kredit_list

        for field in iterable_list:
            month = int(field.split("_")[-1])

            if getattr(self,field + "_active"):
                active_months.append(month)
        
        return active_months[-1]

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