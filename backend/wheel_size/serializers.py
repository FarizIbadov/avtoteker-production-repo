from rest_framework import serializers
from .models import Make,Model,Year,Trim

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ('name','slug')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('name','slug')

    def save(self,**kwargs):
        instance = super().save()
        instance.make = kwargs['make']
        return instance

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('name','slug')

    def save(self,**kwargs):
        instance = super().save()
        instance.make = kwargs['make']
        instance.model = kwargs['model']
        return instance

class TrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trim
        fields = ('name','slug')

    def save(self,**kwargs):
        instance = super().save()
        instance.make = kwargs['make']
        instance.model = kwargs['model']
        instance.year = kwargs['year']
        return instance
