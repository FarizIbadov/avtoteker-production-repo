from django.db import models

class Add(models.Model):
    name = models.CharField(max_length=50,default="advertisement")
    image = models.ImageField(upload_to="add")
    duration = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image.name

