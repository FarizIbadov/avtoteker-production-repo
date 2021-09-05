from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from utils.models import CustomModel

class Kredit(CustomModel):
    slug = models.SlugField()

    title = RichTextField()
    description = RichTextUploadingField()
    order = models.PositiveSmallIntegerField(default=0)
    truncate = models.PositiveSmallIntegerField(default=150)

    link_active = models.BooleanField(default=False)

    def __str__(self):
        return self.slug