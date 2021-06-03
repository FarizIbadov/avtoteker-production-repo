from django import forms
from tireapp.utils import CleanedData
from .models import Oil,Volume,Fuel,Viscosity,OilType


class OilForm(CleanedData,forms.ModelForm):
    volume_text = forms.CharField(label="Volume",max_length=20,widget=forms.TextInput())
    viscosity_text = forms.CharField(label="Viscosity",max_length=20,widget=forms.TextInput())
    fuel_text = forms.CharField(label="Fuel",max_length=50,widget=forms.TextInput())
    oil_type_text = forms.CharField(label="Oil type",max_length=20,widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if kwargs.get("instance"):
            volume = kwargs["instance"].volume
            fuel = kwargs["instance"].fuel
            oil_type = kwargs["instance"].oil_type
            viscosity = kwargs["instance"].viscosity

            if volume:
                self.fields['volume_text'].initial = volume.title
            if fuel:
                self.fields['fuel_text'].initial = fuel.title
            if oil_type:
                self.fields['oil_type_text'].initial = oil_type.title
            if viscosity:
                self.fields['viscosity_text'].initial = viscosity.title


    def save(self, commit=True):
        self.instance.volume = Volume.objects.get_or_create(
            title=self.get_data("volume_text") 
        )[0]


        self.instance.viscosity = Viscosity.objects.get_or_create(
            title=self.get_data("viscosity_text") 
        )[0]

        self.instance.fuel = Fuel.objects.get_or_create(
            title=self.get_data("fuel_text") 
        )[0]

        self.instance.oil_type = OilType.objects.get_or_create(
            title=self.get_data("oil_type_text") 
        )[0]

        self.instance.taksit_2 = self.get_data("taksit_2") or self.get_data("price") / 2
        self.instance.taksit_3 = self.get_data("taksit_3") or self.get_data("price") / 3
        self.instance.taksit_6 = self.get_data("taksit_6") or self.get_data("price") / 6
        self.instance.taksit_9 = self.get_data("taksit_9") or self.get_data("price") / 9
        self.instance.taksit_12 = (
            self.get_data("taksit_12") or self.get_data("price") / 12
        )
        return super().save(commit=commit)

    class Meta:
        model = Oil

        exclude = (
            "taksit_2_month",
            "taksit_3_month",
            "taksit_6_month",
            "taksit_9_month",
            "taksit_12_month",
            "volume",
            'viscosity',
            'fuel',
            'oil_type'
        )