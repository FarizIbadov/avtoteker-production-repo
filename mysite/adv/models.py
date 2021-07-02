from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class CustomValidators:
    @staticmethod
    def check_mime_type(value):
        MIME_TYPES = ['image/svg+xml','image/png','image/jpeg']
        if value._file:
            content_type = value._file.content_type
            try:
                MIME_TYPES.index(content_type)
            except ValueError:
                raise ValidationError("Invalid File")
            
            

class EDVLogo(models.Model):
    logo = models.FileField(upload_to="adv",validators=[
        FileExtensionValidator(allowed_extensions=['svg','png','jpeg','jpg']),
        CustomValidators.check_mime_type
    ])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.logo.name

    def get_url(self):
        return self.logo.url


class EDVPercentage(models.Model):
    first_percentage = models.FloatField()
    second_percentage = models.FloatField()
    active = models.BooleanField(default=True)

    def get_first_perc(self):
        return (self.first_percentage / 100) + 1

    def get_second_perc(self):
        return self.second_percentage / 100

    def __str__(self):
        return f"{self.first_percentage}% - {self.second_percentage}%"



