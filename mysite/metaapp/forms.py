from django import forms
from .models import Meta

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = "__all__"
        widgets = {
            "content":forms.Textarea(attrs={"rows":50,"cols":120})
        } 