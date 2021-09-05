from django.db import models

class Meta(models.Model):
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Meta tags"