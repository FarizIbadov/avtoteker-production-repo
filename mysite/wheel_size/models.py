from django.db import models
from django.urls import reverse
import re

class Make(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    model = models.ForeignKey(Model,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Trim(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    model = models.ForeignKey(Model,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.make,self.name,self.year)

class TireSize(models.Model):
    TYPE_CHOICE = [
        (1,'front'),
        (2,'rear'),
        (3,'4x4')
    ]
    wheel_id = models.CharField(max_length=50)
    tire_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICE)
    tire = models.CharField(max_length=30)
    rim = models.CharField(max_length=30)
    pressure = models.CharField(max_length=50,blank=True)
    
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    model = models.ForeignKey(Model,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    trim = models.ForeignKey(Trim,on_delete=models.CASCADE)


    def __str__(self):
        return "%s | %s | %s" % (
            self.trim,
            self.get_tire_type(),
            self.tire
        )

        
    def get_href(self):
        splited_size_list = re.split(r"/|R|ZR",self.tire)

        width = ""  
        height = ""
        radius = ""

        try:
            width = splited_size_list[0]
        except IndexError:
            width = "_"
            
        try:
            height = splited_size_list[1]
        except IndexError:
            height = "_"

        try:
            radius = splited_size_list[2]
        except IndexError:
            radius = "_"

        url = reverse("detail-list",kwargs={
            "width": width,
            "height": height,
            "radius": radius
        })
        print(url)
        return url

    def get_tire_type(self):
        if self.tire_type == 1:
            return 'Qabaq'
        elif self.tire_type == 2:
            return 'Arxa'
        return "4X4"

