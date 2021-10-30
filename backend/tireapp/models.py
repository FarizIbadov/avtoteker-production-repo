from django.db import models
from datetime import timezone
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from specific.models import Brand, Country, Serie, Season
from app.utils import compress
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.files import File
from utils.models import CustomModel
from sticker.models import Sticker
from campaign.models import Post

from django.utils.translation import gettext as _

class TireClass(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title or '-'


class TireYear(models.Model):
    year = models.PositiveSmallIntegerField(default=2017)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.year)


class OE(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="oe", null=True)

    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "OE"
        verbose_name_plural = "OE"

class Size(CustomModel):
    width = models.CharField(max_length=10, null=True, blank=True) 
    height = models.CharField(max_length=10, null=True, blank=True)
    radius = models.CharField(max_length=10, null=True, blank=True)

    size_code = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "%s\\%s\\%s" % (self.width, self.height, self.radius)

    def get_size_for_title(self):
        return "%s/%s/%s" % (self.width,self.height,self.radius)

    def get_size_for_url(self):
        return "%s-%s-%s" % (self.width,self.height,self.radius)

    def save(self, *args,**kwargs):
        self.size_code = "".join([self.width,self.height,self.radius])
        super().save(*args,**kwargs)



class Tire(CustomModel):
    KREDIT_CHOICES =  [
        (0,"Yoxdur"),
        (3,"3 ay"),
        (6,"6 ay"),
        (9,"9 ay"),
        (12,"12 ay")
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

    code = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True)

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)

    MS = models.BooleanField(default=False)
    OE = models.CharField(max_length=255, default="-")
    SL = models.BooleanField(default=False)
    RF = models.BooleanField(default=False)
    ZR = models.BooleanField(default=False)

    tradeware = models.CharField(max_length=10, null=True)
    weight = models.IntegerField(blank=True)
    speed = models.CharField(max_length=10, blank=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)

    price = models.FloatField(null=True)
    sale = models.FloatField(blank=True, null=True)
    sale_active = models.BooleanField(default=True)
    price_3 = models.FloatField(blank=True,null=True)


    taksit_active = models.BooleanField(default=True)

    taksit_2 = models.FloatField(null=True, blank=True)
    taksit_2_active = models.BooleanField(default=True)

    taksit_3 = models.FloatField(null=True, blank=True)
    taksit_3_active = models.BooleanField(default=True)

    taksit_6 = models.FloatField(null=True, blank=True)
    taksit_6_active = models.BooleanField(default=True)

    taksit_9 = models.FloatField(null=True, blank=True)
    taksit_9_active = models.BooleanField(default=True)

    taksit_12 = models.FloatField(null=True, blank=True)    
    taksit_12_active = models.BooleanField(default=True)

    kredit_active = models.BooleanField(default=True)
    kredit_3 = models.FloatField(null=True, blank=True)
    kredit_3_dif = models.FloatField(default=0)
    kredit_3_active = models.BooleanField(default=True)

    kredit_6 = models.FloatField(null=True, blank=True)
    kredit_6_dif = models.FloatField(default=0)
    kredit_6_active = models.BooleanField(default=True)

    kredit_9 = models.FloatField(null=True, blank=True)
    kredit_9_dif = models.FloatField(default=0)
    kredit_9_active = models.BooleanField(default=True)

    kredit_12 = models.FloatField(null=True, blank=True)
    kredit_12_dif = models.FloatField(default=0)
    kredit_12_active = models.BooleanField(default=True)

    montaj_balance = models.CharField(max_length=255,blank=True, null=True)
    razval = models.CharField(max_length=255,blank=True, null=True)

    year = models.PositiveSmallIntegerField(blank=True, null=True)
    tire_class = models.ForeignKey(TireClass, blank=True, on_delete=models.SET_NULL, null=True)

    quantity = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=255, blank=True,null=True)

    db = models.PositiveSmallIntegerField(default=72)
    fuel = models.CharField(max_length=255, default="B")
    contact = models.CharField(max_length=255, default="B")
    kredit_initial_price = models.FloatField(blank=True, default=0)
    new = models.BooleanField(default=False)
    outlet = models.BooleanField(default=False)

    birkart = models.PositiveSmallIntegerField(choices=BIRKART_CHOICES,blank=True, null=True)
    tamkart = models.PositiveSmallIntegerField(choices=TAMKART_CHOICES,blank=True, null=True)
    bolkart = models.PositiveSmallIntegerField(choices=BOLKART_CHOICES,blank=True, null=True)
    albalikart = models.PositiveSmallIntegerField(choices=ALBALI_CHOICES,blank=True, null=True)
    kredit = models.PositiveSmallIntegerField(choices=KREDIT_CHOICES,blank=True, null=True)

    stickers = models.CharField(max_length=100,blank=True,null=True)
    campaigns = models.CharField(max_length=100,blank=True,null=True)

    @property
    def brand_url(self):
        return self.brand.get_image()


    @property
    def brand_title(self):
        return self.brand.title

    @property
    def free_montaj_balance(self):
        try:
            return round(float(self.montaj_balance), 2)
        except ValueError:
            return False

    def get_stickers(self):
        if self.stickers:
            stickers = self.stickers.split("\\")
            sticker_list = list(filter(None,stickers)) 
            filtered_stickers = list(map(int,sticker_list))
            sticker_qs = Sticker.objects.filter(id__in=filtered_stickers)
            return sticker_qs
        return []

    def get_campaigns(self):
        if self.campaigns:
            campaigns = self.campaigns.split("\\")
            campaign_list = list(filter(None,campaigns)) 
            filtered_campaigns = list(map(int,campaign_list))
            campaign_qs = Post.objects.filter(id__in=filtered_campaigns)
            return campaign_qs
        return []

    def get_tire_info(self):
        return "%s - %s - %s - %s" % (
            self.brand,
            self.serie,
            self.get_size(),
            self.manufacturer,
        )

    def __str__(self):
        return "%s - %s - %s - %s" % (
            self.brand,
            self.serie,
            self.size,
            self.manufacturer,
        )


    def get_absolute_url(self):
        return reverse(
            "detail", kwargs={"pk":self.pk,"slug":self.get_slug()}
        )

    def get_year(self):
        year = TireYear.objects.filter(active=True).first()

        if not year or not self.year:
            return None

        if self.year >= year.year:
            return True

        return False


    def get_OE(self):
        oe = OE.objects.filter(title=self.OE).first()
        return oe
        
    def get_image(self):
        return self.serie.get_image()

    def get_price(self):
        return self.sale if self.sale else self.price

    def get_quantity(self):
        if self.get_quantity_is_numeric():
            return self.quantity if int(self.quantity) <= 4 else "4+"
        else:
            return _("Sorğu ilə")
 
    def get_quantity_is_numeric(self):
        return self.quantity.isnumeric()

    def get_ZR(self):
        return "ZR" if self.ZR else "R"

    def get_size(self):
        return "<span class='text-red'>%s</span>/<span class='text-red'>%s</span> %s<span class='text-red'>%s</span>" % (
            self.size.width,
            self.size.height,
            self.get_ZR(),
            self.size.radius,
        )

    def get_size_for_admin(self):
        return "%s %s %s%s" % (
            self.size.width,
            self.size.height,
            self.size.radius,
            self.get_ZR(),
        )

    def get_percentage(self):
        return ((self.price - self.sale) / self.price) * 100
 
    def get_slug(self):
        if not self.slug:
            self.slug = self.generate_slug()
            self.save()
       
        return self.slug


    def generate_slug(self):
        splited_brand = self.brand.title.lower().split(" ")
        brand = "-".join(splited_brand)

        splited_serie = self.serie.title.lower().split(" ")
        serie = "-".join(splited_serie)

        size = self.size.get_size_for_url()

        slug = "_".join([brand,serie,size]).replace("/","") 
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        if not self.albalikart:
            self.albalikart = self.get_active_price("taksit")
        if not self.tamkart:
            self.tamkart = self.get_active_price("taksit")
        if not self.bolkart:
            self.bolkart = self.get_active_price("taksit")
        if not self.birkart:
            self.birkart = self.get_active_price("taksit")
        if not self.kredit:
            self.kredit = self.get_active_price("kredit")
            
        super().save(*args, **kwargs)


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
        
        return active_months[-1] if len(active_months) != 0 else 0



class OsTireImporterSetting(models.Model):
    look_up = models.CharField(max_length=100, null=True)
    get_from_field = models.CharField(max_length=100, null=True)

    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "OsTire Importer Setting"

            

