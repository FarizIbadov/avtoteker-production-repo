from rest_framework import serializers
from django.utils.translation import gettext as _
from . import models
import phonenumbers

class OilOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        try:
            phone_number = phonenumbers.parse(value,region="AZ")

            if not phonenumbers.is_valid_number(phone_number):
                raise phonenumbers.NumberParseException("error","error")
            return value
        except phonenumbers.NumberParseException:
            message = _("Telefon Nömrə yanlışdı")
            raise serializers.ValidationError(message)

        

    def validate_payment_type(self,value):
        payment_types = [1,2,3]
        try:
            payment_types.index(value)
            return value
        except ValueError:
            message = _("Ödənış üsulu yanlışdı")
            raise serializers.ValidationError(message)

    @property
    def data(self):
        result = models.Result.objects.filter(active=True,order_type="o").first()

        serializer = ResultSerializer(instance=result) 
        return {
            **super().data,
            "result": serializer.data
        }
        

    class Meta:
        model = models.OilOrder
        fields = ('name','oil','phone','email','payment_type','note','order_id')
        read_only_fields = ['order_id']


class TireOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        try:
            phone_number = phonenumbers.parse(value,region="AZ")

            if not phonenumbers.is_valid_number(phone_number):
                raise phonenumbers.NumberParseException("error","error")
            return value
        except phonenumbers.NumberParseException:
            message = _("Telefon Nömrə yanlışdı")
            raise serializers.ValidationError(message)


    def validate_payment_type(self,value):
        payment_types = [1,2,3,4]
        try:
            payment_types.index(value)
            return value
        except ValueError:
            message = _("Ödənış üsulu yanlışdı")
            raise serializers.ValidationError(message)


    def validate_quantity(self,value):
        if value == 0:
            message = _("Sayi zəhmət olmasa təyin edin")
            raise serializers.ValidationError(message)
        return value


    def validate(self, data):
        taksit_choice, payment_choice = data.get("taksit_choice"), data.get("payment_type")
        
        if payment_choice == 4:
            if taksit_choice == 0:
                message = _("Xaiş edirik ayı seçin.")
                raise serializers.ValidationError({"taksit_choice": [message]})

            tire = data.get('tire')
            taksits_raw = tire.get_available_taksit_list().split(",")
            taksits = list(map(int, taksits_raw))

            if not taksit_choice in taksits:
                message = _("Bu taksit seçimi hal hazirda  yoxdı")
                raise serializers.ValidationError({"taksit_choice": [message]})

        return data

    @property
    def data(self):
        result = models.Result.objects.filter(active=True,order_type="t").first()

        serializer = ResultSerializer(instance=result) 
        return {
            **super().data,
            "result": serializer.data
        }

    class Meta:
        model = models.Order
        fields = ('name','tire','phone','email','payment_type','quantity','order_id', "taksit_choice", "lang_code")
        read_only_fields = ['order_id']
        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = ('head','sub','message','order_id_part')