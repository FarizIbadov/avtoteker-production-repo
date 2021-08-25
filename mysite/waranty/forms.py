from django import forms

class WarrantyTireSearchForm(forms.Form):
    code = forms.CharField(max_length=255, required=False)
    size = forms.CharField(max_length=255, required=False)
    brand = forms.CharField(max_length=255, required=False)