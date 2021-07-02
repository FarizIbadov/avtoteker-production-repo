from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from sticker.models import Sticker
from django.conf import settings
import PIL

import os

class CustomValidators:
    @staticmethod
    def check_mime_type(value):
        MIME_TYPES = ["video/mp4"]
        if value._file:
            content_type = value._file.content_type
            try:
                MIME_TYPES.index(content_type)
            except ValueError:
                raise ValidationError("Invalid File")

class Post(models.Model):
    slug = models.CharField(max_length=150)
    title = RichTextField()
    image = models.ImageField(upload_to="campaign/")
    
    description = RichTextUploadingField(blank=True)
    extra = RichTextUploadingField(blank=True)
    extra_2 = RichTextUploadingField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(unique=True)
    truncate = models.PositiveSmallIntegerField(default=150)
    stickers = models.ManyToManyField(Sticker,related_name="posts",blank=True)
    video = models.FileField(upload_to="campaign_video",blank=True,validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return self.slug

