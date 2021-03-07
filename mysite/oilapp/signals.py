from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from .models import Oil, Viscosity


@receiver(post_delete, sender=Oil)
def delete_related_fields(sender, instance, **kwargs):
    try: 
        viscosity = instance.viscosity or None
        if len(viscosity.oil_set.all()) == 0:
            viscosity.delete()
    except Viscosity.DoesNotExist:
        pass


@receiver(post_save, sender=Oil)
def save_existing_oil(sender, instance, created, **kwargs):
    try: 
        if not created:
            for viscosity in Viscosity.objects.all():
                if viscosity and len(viscosity.oil_set.all()) == 0:
                    viscosity.delete()
    except Viscosity.DoesNotExist:
        pass
