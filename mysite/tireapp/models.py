from django.db import models
from datetime import timezone
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from specific.models import Brand, Country, Serie, Season
from mysite.utils import compress
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.files import File
from utils.models import CustomModel
from sticker.models import Sticker
from campaign.models import Post

class Size(CustomModel):
    width = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    radius = models.CharField(max_length=10, null=True)

    def __str__(self):
        return "%s\\%s\\%s" % (self.width, self.height, self.radius)

    def get_size_for_title(self):
        return "%s/%s/%s" % (self.width,self.height,self.radius)

    def get_size_for_url(self):
        return "%s-%s-%s" % (self.width,self.height,self.radius)


class Tire(CustomModel):
    CLASS_CHOICES = [
        (1, "Econom"),
        (2, "Orta"),
        (3, "Premium"),
    ]

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

    code = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(blank=True,max_length=200)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)

    MS = models.BooleanField(default=False)
    OE = models.CharField(default="-",max_length=20)
    SL = models.BooleanField(default=False)
    RF = models.BooleanField(default=False)
    ZR = models.BooleanField(default=False)

    tradeware = models.CharField(max_length=10, null=True)
    weight = models.IntegerField(null=True)
    speed = models.CharField(max_length=10, null=True)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null=True)

    price = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    sale = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    sale_active = models.BooleanField(default=True)

    price_3 = models.FloatField(blank=True,null=True)

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

    kredit_active = models.BooleanField(default=True)

    kredit_3 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    kredit_3_dif = models.FloatField(default=0)
    
    kredit_3_active = models.BooleanField(default=True)

    kredit_6 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    kredit_6_dif = models.FloatField(default=0)
    
    kredit_6_active = models.BooleanField(default=True)

    kredit_9 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    kredit_9_dif = models.FloatField(default=0)
    
    kredit_9_active = models.BooleanField(default=True)

    kredit_12 = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10
    )
    kredit_12_dif = models.FloatField(default=0)
    
    kredit_12_active = models.BooleanField(default=True)

    montaj_balance = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    razval = models.CharField(max_length=50,null=True)

    year = models.PositiveSmallIntegerField(null=True)
    Class = models.PositiveSmallIntegerField(default=1, choices=CLASS_CHOICES)

    quantity = models.PositiveIntegerField(default=4)
    release_date = models.CharField(blank=True,null=True,max_length=30)

    db = models.PositiveSmallIntegerField(default=72)
    fuel = models.CharField(max_length=5,default="B")
    contact = models.CharField(max_length=5,default="B")
    kredit_initial_price = models.FloatField(blank=True,default=0)
    new = models.BooleanField(default=False)
    outlet = models.BooleanField(default=False)

    birkart = models.PositiveSmallIntegerField(choices=BIRKART_CHOICES,blank=True)
    tamkart = models.PositiveSmallIntegerField(choices=TAMKART_CHOICES,blank=True)
    bolkart = models.PositiveSmallIntegerField(choices=BOLKART_CHOICES,blank=True)
    albalikart = models.PositiveSmallIntegerField(choices=ALBALI_CHOICES,blank=True)
    kredit = models.PositiveSmallIntegerField(choices=KREDIT_CHOICES,blank=True)

    stickers = models.CharField(max_length=100,blank=True,null=True)
    campaigns = models.CharField(max_length=100,blank=True,null=True)


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
        
    def get_image(self):
        return self.serie.get_image()

    # def get_edit_url(self):
    #     return reverse(
    #         "custom-admin:tireapp:tire-update", kwargs={"pk": self.id}
    #     )

    # def get_delete_url(self):
    #     return reverse(
    #         "custom-admin:tireapp:tire-delete", kwargs={"pk": self.id}
    #     )

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

    def get_filters(self):
        return "<div>%s</div>  <div class='ml-2'>%s %s</div>"  % (self.year,self.weight,self.speed)

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

    def save(self):
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
        super().save()


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


class OneSTire(models.Model):
    code = models.CharField(max_length=200)
    price_usd = models.PositiveSmallIntegerField(default=0)
    year = models.PositiveSmallIntegerField(null=True,default=timezone.now().year)
    country = models.CharField(max_length=100,blank=True,null=True)
    quantity = models.SmallIntegerField(null=True,default=0)

    def __str__(self):
        return self.code
    

            