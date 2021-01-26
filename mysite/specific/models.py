from django.db import models
from mysite.utils import compress
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Season(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="season", blank=False, null=True)

    def __str__(self):
        return self.title

    def url(self):
        return '<a class="tireapp__table-body-col-link" href=%s>%s</a>' % (
            self.get_absolute_url(),
            self.title,
        )

    def save(self, *args, **kwargs):
        super().save()
        compress(self.image.path, (300, 300))

    def get_absolute_url(self):
        return reverse("custom-admin:specific:season-detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("custom-admin:specific:season-update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("custom-admin:specific:season-delete", kwargs={"pk": self.id})


class Country(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="country", blank=True, null=True)

    def __str__(self):
        return self.title

    def url(self):
        return '<a class="tireapp__table-body-col-link" href=%s>%s</a>' % (
            self.get_absolute_url(),
            self.title,
        )

    def save(self, *args, **kwargs):
        super().save()
        compress(self.image.path, (300, 300))

    def get_absolute_url(self):
        return reverse("custom-admin:specific:country-detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("custom-admin:specific:country-update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("custom-admin:specific:country-delete", kwargs={"pk": self.id})

    class Meta:
        verbose_name_plural = "Countries"


class Brand(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="brand", null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    free_service = models.BooleanField(default=False)
    extra_one_year_warranty = models.CharField(max_length=100,blank=True)
    order_number = models.IntegerField(default=1)
    description = RichTextUploadingField(default="description")
    show_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def url(self):
        return '<a class="tireapp__table-body-col-link" href=%s>%s</a>' % (
            self.get_absolute_url(),
            self.title,
        )

    def save(self, *args, **kwargs):
        super().save()
        compress(self.image.path, (300, 300))

    def get_absolute_url(self):
        return reverse("custom-admin:specific:brand-detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("custom-admin:specific:brand-update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("custom-admin:specific:brand-delete", kwargs={"pk": self.id})


class Serie(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="serie", blank=False, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    dry = models.PositiveSmallIntegerField(default=0)
    wet = models.PositiveSmallIntegerField(default=0)
    offroad = models.PositiveSmallIntegerField(default=0)
    comfort = models.PositiveSmallIntegerField(default=0)
    noise = models.PositiveSmallIntegerField(default=0)
    treadware = models.PositiveSmallIntegerField(default=0)
    snow = models.PositiveSmallIntegerField(default=0)
    value = models.PositiveSmallIntegerField(default=0)
    description = RichTextUploadingField(default="description")
    extra = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    def url(self):
        return '<a class="tireapp__table-body-col-link" href=%s>%s</a>' % (
            self.get_absolute_url(),
            self.title,
        )

    def save(self, *args, **kwargs):
        super().save()
        compress(self.image.path, (300, 300))

    def get_absolute_url(self):
        return reverse("custom-admin:specific:serie-detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("custom-admin:specific:serie-update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("custom-admin:specific:serie-delete", kwargs={"pk": self.id})


Models = {
    "country": Country,
    "season": Season,
    "brand": Brand,
    "serie": Serie,
}
