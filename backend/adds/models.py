from django.db import models
from app.utils import compress

class Add(models.Model):
    name = models.CharField(max_length=50,default="advertisement")
    image = models.ImageField(upload_to="add", null=True)
    duration = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image.name if self.image else '-'

    def get_image(self):
        return self.image.url if self.image else ""

    def save(self, **kwargs):
        super().save(**kwargs)
        compress(self.image.path, quality=90)

