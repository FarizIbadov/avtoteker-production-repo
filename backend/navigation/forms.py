from django import forms
from django.core.validators import ValidationError
from django.urls import reverse, NoReverseMatch
from .models import UrlName

class UrlNameForm(forms.ModelForm):

    def clean(self):
        key = self.cleaned_data.get('key')
        kwargs = self.get_kwargs()

        try:
            reverse(key, kwargs=kwargs)
        except NoReverseMatch:
            self.add_error('key', "Invalid key")

            if kwargs:
                self.add_error("options", "Invalid options")
            
            raise ValidationError("Something went wrong")

    def get_kwargs(self):
        kwargs = {}
        options = self.cleaned_data.get("options")

        if options:
            option_list = options.split(',')

            for option in option_list:
                key, value = option.split(":")
                kwargs[key] = value

        return kwargs



    class Meta:
        model = UrlName
        fields = "__all__"