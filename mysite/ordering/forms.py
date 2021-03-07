from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column,Field
from .models import Order,OilOrder

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1

    
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
                # Column('quantity',css_class="col-md-3")
            ),
            Row(
                # Column('phone',css_class="col-md-6"),
                Column(
                    Field('payment_type',css_class="custom-select"),
                css_class="col-md-9"),
                Column('quantity',css_class="col-md-3")
            ),
        )
        return helper

    class Meta:
        model = Order
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

class OilOrderForm(forms.ModelForm):
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
        model = OilOrder
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