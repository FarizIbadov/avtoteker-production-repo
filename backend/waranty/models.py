from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

from app.validators import ContentTypeValidator, PhoneValidator
from tireapp.models import Tire


class WarrantyTalon(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.car_info.generate_key() if self.car_info else str(self.date)


class PDF(models.Model):
    warranty_talon = models.ForeignKey(
        WarrantyTalon, 
        on_delete=models.CASCADE, 
        null=True,
        related_name="pdf_set"
    )

    file = models.FileField(
        upload_to="pdf", 
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf"]
            ),
            ContentTypeValidator(
                mime_types=["application/pdf"]
            ),
        ]
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.file.name


class CarType(models.Model):
    type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.type

class CarInfo(models.Model):
    warranty_talon = models.OneToOneField(
        WarrantyTalon, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name="car_info"
    )

    full_name = models.CharField("Ad | Soyad",max_length=255, null=True, blank=True)
    phone = models.CharField(
        "Telefon nomrə", max_length=255, null=True, validators=[PhoneValidator], blank=True)
    mileage = models.PositiveIntegerField("Mileage | km", null=True, blank=True)
    wincode = models.CharField("Win | Ban",max_length=255, null=True,  blank=True)


    car_number = models.CharField("Maşın nömrə", max_length=30, blank=True, null=True)
    car_make = models.CharField("Marka", max_length=255, blank=True, null=True)
    car_model = models.CharField("Model", max_length=255, blank=True, null=True)
    car_moter = models.CharField("Motor", max_length=255, blank=True, null=True)
    car_year = models.PositiveSmallIntegerField("İstehsal il", blank=True, null=True)
    car_type = models.ForeignKey(
        CarType, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        verbose_name="Tip"
    )
    year_service = models.BooleanField("1 il servis", default=False)
    gold_warranty = models.BooleanField("Qızıl zemanət", default=False)


    def generate_key(self):
        key_list = self.full_name.split(" ") if self.full_name else []
        date = self.warranty_talon.date

        day = str(date.day) if len(str(date.day)) == 2 else "0" + str(date.day)

        month = str(date.month) if len(str(date.month)) == 2 else "0" + str(date.month)
        phone = self.phone[-4:] if self.phone else ""
        key_list.extend([day, month, phone])
        return "".join(key_list).lower()


class Payment(models.Model):
    warranty_payment_text = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=255, null=True)
    child_of = models.CharField(max_length=255, blank=True, null=True)
    has_childs = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.warranty_payment_text or self.title

    def get_childs(self):
        model_class = self.__class__
        queryset = model_class.objects.filter(child_of=self.key)
        return queryset


    class Meta:
        ordering = ('order',)

class CarTire(models.Model):
    warranty_talon = models.OneToOneField(
        WarrantyTalon, 
        on_delete=models.CASCADE,
        null=True,
        related_name="car_tire"
    )
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE, null=True)

    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, limit_choices_to={"has_childs": False})
    quantity = models.PositiveSmallIntegerField(default=4)
    montaj_balance = models.BooleanField(default=True)
    razval = models.BooleanField(default=True)
    disk_quantity = models.PositiveSmallIntegerField(null=True, blank=True)

    
