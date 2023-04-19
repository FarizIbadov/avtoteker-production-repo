from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = RichTextUploadingField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    
