from django.db import models

class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted=True)

class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model,using=self._db)

    def available(self,*args,**kwargs):
        """
            Returns only delete=False
        """
        return self.filter(deleted=False,*args,**kwargs)

class CustomModel(models.Model):
    deleted = models.BooleanField(default=False)
    objects = CustomManager()

    def delete(self):
        self.deleted = False
        self.save()

    class Meta:
        abstract = True
