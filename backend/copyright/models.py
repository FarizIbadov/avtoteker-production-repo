from django.db import models

class Copyright(models.Model):
    content = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.content