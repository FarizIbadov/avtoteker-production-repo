from django.db import models

class TireListMessage(models.Model):
    text = models.CharField(max_length=255,default="Endirim")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
