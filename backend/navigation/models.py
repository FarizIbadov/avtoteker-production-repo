from django.db import models

class NavigationLink(models.Model):
    title = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=200,null=True)
    order_number = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.title,self.link)

class Logo(models.Model):
    logo = models.ImageField(upload_to="logo")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.logo.url

    def get_name(self):
        return self.logo.name