from django.db import models
from django.urls import reverse
from django.conf import settings

class UrlName(models.Model):
    title = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=255, null=True)

    options = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    @property
    def link(self):
        kwargs = self.get_kwargs()
        return reverse(self.key, kwargs=kwargs)


    def get_kwargs(self):
        kwargs = {}
        if self.options:
            options = self.options.split(',')

            for option in options:
                key, value = option.split(":")
                kwargs[key] = value

        return kwargs


# class NavigationLink(models.Model):
#     title = models.CharField(max_length=20, null=True)
#     url_name = models.ForeignKey(UrlName, on_delete=models.CASCADE, null=True)
#     order_number = models.PositiveSmallIntegerField(default=0)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return "%s - %s" % (self.title, self.link)

#     @property
#     def link(self):
#         return self.url_name.link

class Logo(models.Model):
    logo = models.ImageField(upload_to="logo")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.logo.url

    def get_name(self):
        return self.logo.name

    def get_image_url(self):
        return self.logo.url if self.logo else ""

  