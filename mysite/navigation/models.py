from django.db import models
from utils.models import CustomModel

class NavigationLink(CustomModel):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    order_number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.title,self.link)
