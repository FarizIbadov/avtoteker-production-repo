from django import forms
from tireapp.utils import CleanedData
from .models import Oil


class OilForm(CleanedData,forms.ModelForm):
    def save(self, commit=True):
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
        fields = "__all__"