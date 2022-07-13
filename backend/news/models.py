from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from app.utils import compress
from main_site.models import SessionKey


class News(models.Model):
    slug = models.CharField(max_length=150)
    title = RichTextField()
    image = models.ImageField(upload_to="news/")
    description = RichTextUploadingField(blank=True)
    extra = RichTextUploadingField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(unique=True)
    truncate = models.PositiveSmallIntegerField(default=150)

    viewed_by = models.ManyToManyField(SessionKey, editable=False)

    created_at = models.DateTimeField(auto_now=True, null=True)



    def __str__(self):
        return self.slug

    def save(self):
        super().save()

        compress(self.image.path,quality=90)

    

    class Meta:
        verbose_name_plural = "News"

