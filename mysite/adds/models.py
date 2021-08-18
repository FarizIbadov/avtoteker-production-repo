from django.db import models
from mysite.utils import compress

class Add(models.Model):
    name = models.CharField(max_length=50,default="advertisement")
    image = models.ImageField(upload_to="add")
    duration = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image.name

    def save(self, **kwargs):
        super().save(**kwargs)

        compress(self.image.path, quality=90)

