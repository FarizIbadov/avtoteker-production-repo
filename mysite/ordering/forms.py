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

    name = forms.CharField(max_length=20,label="Ad:")
    quantity = forms.IntegerField(min_value=1,label="Say:",required=True)
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES,)
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Ordering nothing?")
        return quantity

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

    class Meta:
        exclude = ('is_purchased','order_date',)
        widgets = {
            "quantity": forms.NumberInput(),
            "is_purchased": forms.HiddenInput(),
            "tire": forms.HiddenInput(),
        }
        labels = {
            "name":"Ad:",
            "quantity":"Say:",
            "payment_type":"Ödənış üsulu:",
            "phone":"Mobil nömrəsi:"
        }

class OilOrderForm(forms.Form):
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

    class Meta:
        exclude = ('is_purchased','order_date',)
        widgets = {
            "quantity": forms.NumberInput(),
            "is_purchased": forms.HiddenInput(),
            "oil": forms.HiddenInput(),
        }
        labels = {
            "name":"Ad:",
            "payment_type":"Ödənış üsulu:",
            "phone":"Mobil nömrəsi:",
            "note": "İstəyinizi yazın:"
        }