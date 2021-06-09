from rest_framework import serializers
from . import models
import re

class OilOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        phone_re = re.compile(r"\d+")
        phone_re_split = re.compile(r"\s|-")
        phone = value

        if phone.find('+') == 0:
            phone = phone[1:]

        phone = phone_re_split.split(phone)
        phone = "".join(phone)

        if not phone_re.search(phone):
            raise serializers.ValidationError("Telefon Nömrə yanlışdı")
            
        return value

    def validate_payment_type(self,value):
        payment_types = [1,2,3]
        try:
            payment_types.index(value)
            return value
        except ValueError:
            raise serializers.ValidationError("Ödənış üsulu yanlışdı")
        

    class Meta:
        model = models.OilOrder
        fields = ('name','oil','phone','payment_type','note')


class TireOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        phone_re = re.compile(r"\d+")
        phone_re_split = re.compile(r"\s|-")
        phone = value

        if phone.find('+') == 0:
            phone = phone[1:]

        phone = phone_re_split.split(phone)
        phone = "".join(phone)

        if not phone_re.search(phone):
            raise serializers.ValidationError("Telefon Nömrə yanlışdı")
            
        return value

    def validate_payment_type(self,value):
        payment_types = [1,2,3,4]
        try:
            payment_types.index(value)
            return value
        except ValueError:
            raise serializers.ValidationError("Ödənış üsulu yanlışdı")

    def validate_quantity(self,value):
        if value == 0:
            raise serializers.ValidationError("Sayi zəhmət olmasa təyin edin")
        return value

    class Meta:
        model = models.Order
        fields = ('name','tire','phone','payment_type','quantity')