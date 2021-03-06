from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column,Field
from .models import Order,OilOrder

class OrderForm(forms.Form):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'Kreditlə'),
        (4,'BirKart / TamKart ilə'),
    ]

    name = forms.CharField(max_length=20,label="Ad:",required=False)
    quantity = forms.IntegerField(min_value=1,label="Say:",required=True,widget=forms.NumberInput(attrs={"value": 1}))
    payment_type = forms.ChoiceField(label="Ödənış üsulu:",choices=PAYMENT_CHOICES,required=True)
    phone = forms.CharField(label="Mobil nömrəsi:",max_length=20,required=True)
    tire = forms.IntegerField(min_value=0,widget=forms.HiddenInput())


    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.layout = Layout(
            'tire',
            Row(
                Column('name',css_class="col-md"),
                Column('phone',css_class="col-md"),
            ),
            Row(
                Column(
                    Field('payment_type',css_class="custom-select"),
                css_class="col-md-9"),
                Column('quantity',css_class="col-md-3")
            ),
        )
        return helper

class OilOrderForm(forms.Form):
    PAYMENT_CHOICES = [
        (1,'Nağd'),
        (2,'Kart ilə'),
        (3,'BirKart / TamKart ilə'),
    ]

    name = forms.CharField(max_length=20,label="Ad:",required=False)
    quantity = forms.IntegerField(min_value=1,label="Say:",required=True)
    payment_type = forms.ChoiceField(label="Ödənış üsulu:",choices=PAYMENT_CHOICES,required=True)
    phone = forms.CharField(label="Mobil nömrəsi:",max_length=20,required=True)
    oil = forms.IntegerField(min_value=0,widget=forms.HiddenInput())
    note = forms.CharField(label="İstəyinizi yazın:",widget=forms.Textarea,required=False)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.layout = Layout(
            'oil',
            Row(
                Column('name',css_class="col-md"),
                Column('phone',css_class="col-md"),
            ),
            Row(
                Column(
                    Field('payment_type',css_class="custom-select"),
                css_class="col-md")
            ),
            Row(
                Column('note',css_class="col-md")
            ),
        )
        return helper