from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from import_export.forms import ImportForm 

from .models import Tire, Size
from specific.models import Brand
from .utils import CleanedData
from django.utils.html import escape
from specific.models import Season


class TireForm(forms.ModelForm):
    width = forms.CharField(widget=forms.TextInput(), required=False)
    height = forms.CharField(max_length=10, widget=forms.TextInput(), required=False)
    radius = forms.CharField(widget=forms.TextInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get("instance"):
            size = kwargs["instance"].size
            if size:
                self.fields["width"].initial = size.width
                self.fields["height"].initial = size.height
                self.fields["radius"].initial = size.radius

    def save(self, commit=True):
        self.instance.size = Size.objects.get_or_create(
            width=self.cleaned_data.get("width"),
            height=self.cleaned_data.get("height"),
            radius=self.cleaned_data.get("radius"),
        )[0]
        self.instance.kredit_3 = self.cleaned_data.get("kredit_3") or self.cleaned_data.get("price") / 3
        self.instance.kredit_6 = self.cleaned_data.get("kredit_6") or self.cleaned_data.get("price") / 6
        self.instance.kredit_9 = self.cleaned_data.get("kredit_9") or self.cleaned_data.get("price") / 9
        self.instance.kredit_12 = (
            self.cleaned_data.get("kredit_12") or self.cleaned_data.get("price") / 12
        )
        self.instance.taksit_2 = self.cleaned_data.get("taksit_2") or self.cleaned_data.get("price") / 2
        self.instance.taksit_3 = self.cleaned_data.get("taksit_3") or self.cleaned_data.get("price") / 3
        self.instance.taksit_6 = self.cleaned_data.get("taksit_6") or self.cleaned_data.get("price") / 6
        self.instance.taksit_9 = self.cleaned_data.get("taksit_9") or self.cleaned_data.get("price") / 9
        self.instance.taksit_12 = (
            self.cleaned_data.get("taksit_12") or self.cleaned_data.get("price") / 12
        )
        return super().save(commit=commit)

    class Meta:
        model = Tire
        exclude = ("size",)

        widgets = {
            "brand": forms.Select(attrs={"class": "custom-select"}),
            "serie": forms.Select(attrs={"class": "custom-select"}),
            "manufacturer": forms.Select(attrs={"class": "custom-select"}),
            "season": forms.Select(attrs={"class": "custom-select"}),
            "Class": forms.Select(attrs={"class": "custom-select"}),
            "description": forms.Textarea(attrs={"rows": 7}),
            "width": forms.TextInput(),
            "height": forms.TextInput(),
            "radius": forms.TextInput(),
            "weight": forms.TextInput(),
            "montaj_balance": forms.TextInput(),
            "razval": forms.TextInput(),
            "year": forms.TextInput(),
            "USDNO": forms.TextInput(),
            "USD": forms.TextInput(),
            "USDOFF": forms.TextInput(),
            "kredit_3": forms.TextInput(),
            "kredit_3_dif": forms.TextInput(),
            "kredit_6": forms.TextInput(),
            "kredit_6_dif": forms.TextInput(),
            "kredit_9": forms.TextInput(),
            "kredit_9_dif": forms.TextInput(),
            "kredit_12": forms.TextInput(),
            "kredit_12_dif": forms.TextInput(),
            "taksit_2": forms.TextInput(),
            "taksit_2_dif": forms.TextInput(),
            "taksit_3": forms.TextInput(),
            "taksit_3_dif": forms.TextInput(),
            "taksit_6": forms.TextInput(),
            "taksit_6_dif": forms.TextInput(),
            "taksit_9": forms.TextInput(),
            "taksit_9_dif": forms.TextInput(),
            "taksit_12": forms.TextInput(),
            "taksit_12_dif": forms.TextInput(),
        }

class TireImportForm(ImportForm):
    # detail = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # if self.fields['detail'].initial is None:
        #     self.fields['detail'].initial = True

class OsImportform(ImportForm):
    pass
    # brands = forms.ModelChoiceField(
    #     queryset=Brand.objects.available(), 
    #     widget=forms.CheckboxSelectMultiple(),
    #     required=False,
    #     blank=True
    # )
