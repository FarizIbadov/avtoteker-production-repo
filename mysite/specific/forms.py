from django import forms
from django.urls import reverse_lazy
from specific.models import Country, Season, Serie, Brand
from django.utils.html import escape
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Div, HTML, Field
from mysite.utils import get_submit_label, get_prev_url, get_button_container


class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submit_label = get_submit_label(kwargs)
        self.prev_url = get_prev_url(**kwargs, list_url="custom-admin:specific:country")


    @property
    def helper(self):
        helper = FormHelper()
        prev_url, submit_label = self.prev_url, self.submit_label
        helper.attrs = {"novalidate": True}
        helper.use_custom_control = True
        helper.form_class = "specific-form"
        helper.layout = Layout(
            "title", "image", get_button_container(submit_label, prev_url)
        )
        return helper

    class Meta:
        model = Country
        fields = "__all__"


class SeasonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submit_label = get_submit_label(kwargs)
        self.prev_url = get_prev_url(**kwargs, list_url="custom-admin:specific:season")


    @property
    def helper(self):
        helper = FormHelper()
        prev_url, submit_label = self.prev_url, self.submit_label
        helper.attrs = {"novalidate": True}
        helper.use_custom_control = True
        helper.form_class = "needs-validation"
        helper.layout = Layout(
            "title", "image", get_button_container(submit_label, prev_url)
        )
        return helper

    class Meta:
        model = Season
        fields = "__all__"


class BrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submit_label = get_submit_label(kwargs)
        self.prev_url = get_prev_url(**kwargs, list_url="custom-admin:specific:brand")

    @property
    def helper(self):
        helper = FormHelper()
        prev_url, submit_label = self.prev_url, self.submit_label
        helper.attrs = {"novalidate": True}
        helper.use_custom_control = True
        helper.form_class = "needs-validation"
        helper.layout = Layout(
            "title",
            "image",
            Field("country", css_class="custom-select"),
            "order_number",
            "description",
            'free_service',
            "extra_one_year_warranty",
            "show_in_slider",
            get_button_container(submit_label, prev_url),
        )
        return helper


    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {"order_number": forms.TextInput()}


class SerieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submit_label = get_submit_label(kwargs)
        self.prev_url = get_prev_url(**kwargs, list_url="custom-admin:specific:serie")
        self.fields['dry'].widget.attrs['max'] = 5
        self.fields['dry'].widget.attrs['step'] = 1
        self.fields['wet'].widget.attrs['max'] = 5
        self.fields['wet'].widget.attrs['step'] = 1
        self.fields['offroad'].widget.attrs['max'] = 5
        self.fields['offroad'].widget.attrs['step'] = 1
        self.fields['comfort'].widget.attrs['max'] = 5
        self.fields['comfort'].widget.attrs['step'] = 1
        self.fields['snow'].widget.attrs['max'] = 5
        self.fields['snow'].widget.attrs['step'] = 1
        self.fields['noise'].widget.attrs['max'] = 5
        self.fields['noise'].widget.attrs['step'] = 1
        self.fields['treadware'].widget.attrs['max'] = 5
        self.fields['treadware'].widget.attrs['step'] = 1
        self.fields['value'].widget.attrs['max'] = 5
        self.fields['value'].widget.attrs['step'] = 1

    @property
    def helper(self):
        helper = FormHelper()
        prev_url, submit_label = self.prev_url, self.submit_label
        helper.attrs = {"novalidate": True}
        helper.use_custom_control = True
        helper.form_class = "needs-validation"
        helper.layout = Layout(
            "title",
            "image",
            "dry",
            'wet',
            'offroad',
            'comfort',
            "snow",
            'noise',
            'treadware',
            'value',
            Field("brand", css_class="custom-select"),
            "description",
            'extra',
            get_button_container(submit_label, prev_url),
        )
        return helper

    class Meta:
        model = Serie
        fields = "__all__"


Forms = {
    "country": CountryForm,
    "season": SeasonForm,
    "brand": BrandForm,
    "serie": SerieForm,
}
