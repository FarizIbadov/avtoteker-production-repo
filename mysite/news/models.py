from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    slug = models.CharField(max_length=150)
    title = RichTextField()
    image = models.ImageField(upload_to="news/")
    description = RichTextUploadingField(blank=True)
    extra = RichTextUploadingField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(unique=True)
    truncate = models.PositiveSmallIntegerField(default=150)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "News"

