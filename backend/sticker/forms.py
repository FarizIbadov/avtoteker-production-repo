from django import forms
from . import models

class RangeInput(forms.NumberInput):
    input_type = 'range'

class StickerForm(forms.ModelForm):
    class Meta:
        model = models.Sticker
        fields = "__all__"
        widgets = {
            "image_width":RangeInput,
            "text_width":RangeInput,
        }

