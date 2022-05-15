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
        
        return super().save(commit=commit)

    class Meta:
        model = Tire
        exclude = ("size",)

class TireImportForm(ImportForm):
    # detail = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # if self.fields['detail'].initial is None:
        #     self.fields['detail'].initial = True

class OsImportform(ImportForm):
    pass