from django.db import models
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField

class Sticker(models.Model):
    color = ColorField(default="#cccccc")
    image = models.ImageField(upload_to="sticker", blank=True)
    image_width = models.FloatField(default=50)
    text = models.CharField(max_length=20)
    text_font = models.PositiveSmallIntegerField(default=16)
    text_width = models.FloatField(default=50)
    active = models.BooleanField(default=True)

    description = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.text

    def get_image(self):
        return self.image.url if self.image else ""

    def get_content(self):
        return self.description or self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.image_width + self.text_width == 100:
            if self.image_width > self.text_width:
                self.text_width = 100 - self.image_width
            else:
                self.image_width = 100 - self.text_width

        super().save(force_insert, force_update, using, update_fields)

class StickerTimer(models.Model):
    interval = models.PositiveSmallIntegerField(default=2000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.interval)