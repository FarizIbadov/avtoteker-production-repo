from django.db import models
from django.core.exceptions import ValidationError


class Favicon(models.Model):
    icon = models.FileField(upload_to='favicon')
    active = models.BooleanField(default=True)

    def clean(self,*args, **kwargs):
        extension = self.icon.name.split('.')[-1]
        if extension != 'ico':
            raise ValidationError('Please provide an ico file')
        super(Favicon, self).clean(*args, **kwargs)

    def __str__(self):
        return self.icon.name