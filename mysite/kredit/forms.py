from django import forms

class OnlineKreditForm(forms.ModelForm):
    class Meta:
        model = OnlineKredit
        fields = "__all__"