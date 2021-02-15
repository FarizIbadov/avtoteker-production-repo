from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from .models import Tire, Size


@receiver(post_delete, sender=Tire)
def delete_related_fields(sender, instance: Tire, **kwargs):
    try: 
        size = instance.size or None
        if len(size.tire_set.all()) == 0:
            size.delete()
    except Size.DoesNotExist:
        pass


@receiver(post_save, sender=Tire)
def save_existing_tire(sender, instance, created, **kwargs):
    try: 
        if not created:
            for size in Size.objects.all():
                if size and len(size.tire_set.all()) == 0:
                    size.delete()
    except Size.DoesNotExist:
        pass
