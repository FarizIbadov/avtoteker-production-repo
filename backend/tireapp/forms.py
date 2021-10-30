from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Tire, Size
from .utils import CleanedData
from django.utils.html import escape
from specific.models import Season
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML, Field, Button
from app.utils import get_button_container


class TireForm(forms.ModelForm):
    width = forms.CharField(widget=forms.TextInput(), required=False)
    height = forms.CharField(max_length=10, widget=forms.TextInput(), required=False)
    radius = forms.CharField(widget=forms.TextInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.submit_label = "Add"
        # self.prev_url = reverse("custom-admin:tireapp:home")

        if kwargs.get("instance"):
            # self.submit_label = "Update"
            # self.prev_url = reverse("custom-admin:tireapp:tire-detail",kwargs={'pk':kwargs["instance"].id})
            size = kwargs["instance"].size
            if size:
                self.fields["width"].initial = size.width
                self.fields["height"].initial = size.height
                self.fields["radius"].initial = size.radius

    def save(self, commit=True):
        self.instance.size = Size.objects.get_or_create(
            width=self.cleaned_data.get("width"),
            height=self.cleaned_data.get("height"),
            radius=self.cleaned_data.get("radius"),
        )[0]
        self.instance.kredit_3 = self.cleaned_data.get("kredit_3") or self.cleaned_data.get("price") / 3
        self.instance.kredit_6 = self.cleaned_data.get("kredit_6") or self.cleaned_data.get("price") / 6
        self.instance.kredit_9 = self.cleaned_data.get("kredit_9") or self.cleaned_data.get("price") / 9
        self.instance.kredit_12 = (
            self.cleaned_data.get("kredit_12") or self.cleaned_data.get("price") / 12
        )
        self.instance.taksit_2 = self.cleaned_data.get("taksit_2") or self.cleaned_data.get("price") / 2
        self.instance.taksit_3 = self.cleaned_data.get("taksit_3") or self.cleaned_data.get("price") / 3
        self.instance.taksit_6 = self.cleaned_data.get("taksit_6") or self.cleaned_data.get("price") / 6
        self.instance.taksit_9 = self.cleaned_data.get("taksit_9") or self.cleaned_data.get("price") / 9
        self.instance.taksit_12 = (
            self.cleaned_data.get("taksit_12") or self.cleaned_data.get("price") / 12
        )
        return super().save(commit=commit)

    # @property
    # def helper(self):
    #     helper = FormHelper()
    #     helper.attrs = {"novalidate": ""}
    #     helper.form_class = "needs-validation"
    #     helper.layout = Layout(
    #         Row(
    #             Column("brand"),
    #             Column("serie"),
    #             Column("manufacturer"),
    #             Column("season"),
    #         ),
    #         Row(
    #             Column("width"),
    #             Column("height"),
    #             Column("radius"),
    #         ),
    #         Row(
    #             Column(
    #                 Row(
    #                     Column("ZR"),
    #                     Column("MS"),
    #                     Column("RF"),
    #                     Column("SL"),
    #                     css_class="justify-content-between w-100",
    #                 ),
    #                 css_class="d-flex align-items-center",
    #             ),
    #             Column(
    #                 Row(
    #                     Column("OE"),
    #                     Column("tradeware"),
    #                     Column("weight"),
    #                     Column("speed"),
    #                 )
    #             ),
    #         ),
    #         Row(
    #             Column("montaj_balance"),
    #             Column("razval"),
    #             Column("year"),
    #             Column("Class"),
    #         ),
    #         Row(
    #             Column("USDNO"),
    #             Column("USD", "USD_active"),
    #             Column("USDOFF", "USDOFF_active"),
    #         ),
    #         Row(
    #             Column(
    #                 HTML("<h2 style='margin-right:10px;'>Kredit</h2>"), 
    #                 Field("kredit_active"), css_class="tireapp-form__col"
    #             ),
    #             css_class="mb-2",
    #         ),
    #         Row(
    #             Column(
    #                 Field("kredit_3", css_class="form-control-sm"),
    #                 Field("kredit_3_dif", css_class="form-control-sm"),
    #                 "kredit_3_active",
    #             ),
    #             Column(
    #                 Field("kredit_6", css_class="form-control-sm"),
    #                 Field("kredit_6_dif", css_class="form-control-sm"),
    #                 "kredit_6_active",
    #             ),
    #             Column(
    #                 Field("kredit_9", css_class="form-control-sm"),
    #                 Field("kredit_9_dif", css_class="form-control-sm"),
    #                 "kredit_9_active",
    #             ),
    #             Column(
    #                 Field("kredit_12", css_class="form-control-sm"),
    #                 Field("kredit_12_dif", css_class="form-control-sm"),
    #                 "kredit_12_active",
    #             ),
    #         ),
    #         Row(
    #             Column(
    #                 HTML("<h2 style='margin-right:10px;'>Taksit</h2>"), "taksit_active", css_class="tireapp-form__col"
    #             ),
    #             css_class="mb-2 tireapp-form__col",
    #         ),
    #         Row(
    #             Column(
    #                 Field("taksit_2", css_class="form-control-sm"), "taksit_2_active"
    #             ),
    #             Column(
    #                 Field("taksit_3", css_class="form-control-sm"), "taksit_3_active"
    #             ),
    #             Column(
    #                 Field("taksit_6", css_class="form-control-sm"), "taksit_6_active"
    #             ),
    #             Column(
    #                 Field("taksit_9", css_class="form-control-sm"), "taksit_9_active"
    #             ),
    #             Column(
    #                 Field("taksit_12", css_class="form-control-sm"), "taksit_12_active"
    #             ),
    #         ),
    #         'release_date',
    #         "kredit_initial_price",
    #         Row(
    #             Column("db"),
    #             Column("fuel"),
    #             Column("contact")
    #         ),
    #         Row(
    #             Column(
    #                 "image",
    #                 "quantity",
    #                 get_button_container(
    #                     self.submit_label, self.prev_url, "tireapp-form__btn-group"
    #                 ),
    #             ),
    #         ),
    #     )
    #     return helper

    class Meta:
        model = Tire
        exclude = ("size",)

        widgets = {
            "brand": forms.Select(attrs={"class": "custom-select"}),
            "serie": forms.Select(attrs={"class": "custom-select"}),
            "manufacturer": forms.Select(attrs={"class": "custom-select"}),
            "season": forms.Select(attrs={"class": "custom-select"}),
            "Class": forms.Select(attrs={"class": "custom-select"}),
            "description": forms.Textarea(attrs={"rows": 7}),
            "width": forms.TextInput(),
            "height": forms.TextInput(),
            "radius": forms.TextInput(),
            "weight": forms.TextInput(),
            "montaj_balance": forms.TextInput(),
            "razval": forms.TextInput(),
            "year": forms.TextInput(),
            "USDNO": forms.TextInput(),
            "USD": forms.TextInput(),
            "USDOFF": forms.TextInput(),
            "kredit_3": forms.TextInput(),
            "kredit_3_dif": forms.TextInput(),
            "kredit_6": forms.TextInput(),
            "kredit_6_dif": forms.TextInput(),
            "kredit_9": forms.TextInput(),
            "kredit_9_dif": forms.TextInput(),
            "kredit_12": forms.TextInput(),
            "kredit_12_dif": forms.TextInput(),
            "taksit_2": forms.TextInput(),
            "taksit_2_dif": forms.TextInput(),
            "taksit_3": forms.TextInput(),
            "taksit_3_dif": forms.TextInput(),
            "taksit_6": forms.TextInput(),
            "taksit_6_dif": forms.TextInput(),
            "taksit_9": forms.TextInput(),
            "taksit_9_dif": forms.TextInput(),
            "taksit_12": forms.TextInput(),
            "taksit_12_dif": forms.TextInput(),
        }

        # labels = {
        #     "USDNO": "Price",
        #     "USD": "Sale",
        #     "USDOFF": "Price Difference",
        #     "kredit_3": "3 month",
        #     "kredit_3_dif": "Rise in price",
        #     "kredit_6": "6 month",
        #     "kredit_6_dif": "Rise in price",
        #     "kredit_9": "9 month",
        #     "kredit_9_dif": "Rise in price",
        #     "kredit_12": "12 month",
        #     "kredit_12_dif": "Rise in price",
        #     "taksit_2": "2 month",
        #     "taksit_3": "3 month",
        #     "taksit_6": "6 month",
        #     "taksit_9": "9 month",
        #     "taksit_12": "12 month",
        #     "USD_active": "active",
        #     "USDOFF_active": "active",
        #     "kredit_active": "active",
        #     "kredit_3_active": "active",
        #     "kredit_6_active": "active",
        #     "kredit_9_active": "active",
        #     "kredit_12_active": "active",
        #     "taksit_active": "active",
        #     "taksit_2_active": "active",
        #     "taksit_3_active": "active",
        #     "taksit_6_active": "active",
        #     "taksit_9_active": "active",
        #     "taksit_12_active": "active",
        # }


# class ExcelImportForm(forms.Form):
#     _file = forms.FileField(
#         label="",
#         required=True,
#         widget=forms.ClearableFileInput(attrs={"accept": ".xlsx, .xls"}),
#     )

#     @property
#     def helper(self):
#         helper = FormHelper()
#         helper.attrs = {"novalidate": ""}
#         helper.form_class = "needs-validation"
#         helper._form_action = reverse("custom-admin:tireapp:excel")
#         helper.layout = Layout(
#             Row(
#                 Column("_file", css_class="col-md-4 mt-2"),
#                 Column(
#                     Submit("submit", "Import", css_class="btn-my-secondary btn-block"),
#                     css_class="col-md-3 mt-2",
#                 ),
#             )
#         )
#         return helper

#     def clean__file(self):
#         extensions = ["xls", "xlsx"]
#         data = self.cleaned_data.get("_file")
#         ext = data._name.split(".")[-1]

#         if ext in extensions:
#             return data
#         else:
#             return ValidationError("Invalid file!")


# class ExcelExportForm(forms.Form):
#     file_format = forms.ChoiceField(
#         label="",
#         choices=(
#             [
#                 ("xls", "xls"),
#                 ("xlsx", "xlsx"),
#             ]
#         ),
#         widget=forms.Select(attrs={"class": "custom-select"}),
#     )

#     @property
#     def helper(self):
#         helper = FormHelper()
#         helper.attrs = {"novalidate": ""}
#         helper.form_method = "GET"
#         helper._form_action = reverse("custom-admin:tireapp:excel")
#         helper.layout = Layout(
#             Row(
#                 Column(
#                     Submit(
#                         "submit", "Export", css_class="btn-my-primary mt-2  btn-block"
#                     ),
#                     css_class="col-md-3 d-flex justify-content-end align-items-start",
#                 ),
#                 Column("file_format", css_class="col-md-4 mt-2"),
#                 css_class="justify-content-end",
#             )
#         )
#         return helper


# class PaginateByForm(forms.Form):
#     word = "items"
#     per_page = forms.ChoiceField(
#         label="",
#         choices=(
#             [
#                 (100, "Items per page"),
#                 (10, f"10 {word}"),
#                 (25, f"25 {word}"),
#                 (50, f"50 {word}"),
#                 (100, f"100 {word}"),
#             ]
#         ),
#         widget=forms.Select(attrs={"class": "custom-select"}),
#         required=False,
#     )

#     @property
#     def helper(self):
#         helper = FormHelper()
#         helper.attrs = {"novalidate": ""}
#         helper.form_method = "GET"
#         helper.layout = Layout(
#             Row(
#                 Column("per_page", css_class="col-md-2 my-2 align-items-center"),
#                 Column(
#                     HTML(
#                         '<button type="submin" class="btn btn-my-primary btn-block">Paginate</button>',
#                     ),
#                     css_class="col-md-2 d-flex align-items-center my-2",
#                 ),
#                 css_class="mb-3",
#             )
#         )
#         return helper


# class ExcelForms:
#     def __init__(self):
#         self.imports = ExcelImportForm
#         self.exports = ExcelExportForm
