from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from .models import Oil, Viscosity,OilType,Fuel,Volume


@receiver(post_delete, sender=Oil)
def delete_related_fields(sender, instance, **kwargs):
    try: 
        viscosity = instance.viscosity or None
        fuel = instance.fuel or None
        oil_type = instance.oil_type or None
        volume = instance.volume or None

        if len(viscosity.oil_set.all()) == 0:
            viscosity.delete()

        if len(fuel.oil_set.all()) == 0:
            fuel.delete()

        if len(oil_type.oil_set.all()) == 0:
            oil_type.delete()

        if len(volume.oil_set.all()) == 0:
            volume.delete()

    except Viscosity.DoesNotExist:
        pass
    except Volume.DoesNotExist:
        pass
    except OilType.DoesNotExist:
        pass
    except Fuel.DoesNotExist:
        pass


@receiver(post_save, sender=Oil)
def save_existing_oil(sender, instance, created, **kwargs):
    try: 
        if not created:
            for viscosity in Viscosity.objects.all():
                if viscosity and len(viscosity.oil_set.all()) == 0:
                    viscosity.delete()
                    
            for fuel in Fuel.objects.all():
                if fuel and len(fuel.oil_set.all()) == 0:
                    fuel.delete()

            for oil_type in OilType.objects.all():
                if oil_type and len(oil_type.oil_set.all()) == 0:
                    oil_type.delete()

            for volume in Volume.objects.all():
                if volume and len(volume.oil_set.all()) == 0:
                    volume.delete()

    except Viscosity.DoesNotExist:
        pass
    except Volume.DoesNotExist:
        pass
    except OilType.DoesNotExist:
        pass
    except Fuel.DoesNotExist:
        pass
