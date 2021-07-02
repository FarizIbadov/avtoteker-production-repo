from django.db import models
from django.http import Http404

class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted=True)

    def backup(self):
        self.update(deleted=False)


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model,using=self._db)

    def available(self,*args,**kwargs):
        kwargs['deleted'] = False
        return self.filter(*args,**kwargs)

    def get(self, *args, **kwargs):
        kwargs['deleted'] = False
        instance = self.get_object(*args, **kwargs)
        return instance

    def get_object(self,*args,**kwargs):
        return super().get(*args, **kwargs)

class CustomModel(models.Model):
    deleted = models.BooleanField(default=False)
    objects = CustomManager()

    def delete(self):
        self.deleted = True
        self.save()

    def backup(self):
        self.deleted = False
        self.save()

    class Meta:
        abstract = True