from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers
from . import models
from emailapp.models import AuthUser,Email
import phonenumbers

class OilOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        try:
            phone_number = phonenumbers.parse(value,region="AZ")

            if not phonenumbers.is_valid_number(phone_number):
                raise phonenumbers.NumberParseException("error","error")
            return value
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Telefon Nömrə yanlışdı")
            
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        self.perform_email_send(instance)
        return instance

    
    def perform_email_send(self,instance):
        auth_user = AuthUser.objects.filter(active=True).first()
        if auth_user:
            recipient_list = Email.objects.all().values_list("email",flat=True)
            kwargs = {
                "fail_silently": not settings.DEBUG,
                "subject": "Order",
                "message": "OK",
                "auth_user": auth_user.email,
                "auth_password": auth_user.password,
                "from_email": auth_user.email,
                "recipient_list": list(recipient_list)
            }
            send_mail(**kwargs)
        

    def validate_payment_type(self,value):
        payment_types = [1,2,3]
        try:
            payment_types.index(value)
            return value
        except ValueError:
            raise serializers.ValidationError("Ödənış üsulu yanlışdı")

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
        fields = ('name','oil','phone','payment_type','note','order_id')
        read_only_fields = ['order_id']


class TireOrderSerializer(serializers.ModelSerializer):
    def validate_phone(self,value):
        try:
            phone_number = phonenumbers.parse(value,region="AZ")

            if not phonenumbers.is_valid_number(phone_number):
                raise phonenumbers.NumberParseException("error","error")
            return value
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Telefon Nömrə yanlışdı")

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        self.perform_email_send(instance)
        return instance

    def perform_email_send(self,instance):
        auth_user = AuthUser.objects.filter(active=True).first()
        if auth_user:
            recipient_list = Email.objects.all().values_list("email",flat=True)
            kwargs = {
                "fail_silently": not settings.DEBUG,
                "subject": "Order",
                "message": "OK",
                "auth_user": auth_user.email,
                "auth_password": auth_user.password,
                "from_email": auth_user.email,
                "recipient_list": list(recipient_list)
            }
            send_mail(**kwargs)

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
        fields = ('name','tire','phone','payment_type','quantity','order_id')
        read_only_fields = ['order_id']
        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = ('head','sub','order_id_part')