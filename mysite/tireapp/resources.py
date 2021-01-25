from import_export import resources, fields
from .models import Tire
from . import widgets
from import_export import widgets as resource_widget


class TireResource(resources.ModelResource):
    def get_queryset(self):
        return self.Meta.model.objects.all().order_by("id")

    origin = fields.Field(
        attribute="brand__country", widget=widgets.CustomCountryWidget()
    )
    manufacturer = fields.Field(
        attribute="manufacturer", widget=widgets.CustomCountryWidget()
    )
    season = fields.Field(attribute="season", widget=widgets.CustomSeasonWidget())
    brand = fields.Field(attribute="brand", widget=widgets.CustomBrandWidget())
    serie = fields.Field(attribute="serie", widget=widgets.CustomSerieWidget())
    

    ZR = fields.Field(attribute="ZR", widget=widgets.CustomBooleanWidget())
    MS = fields.Field(
        column_name="M+S", attribute="MS", widget=widgets.CustomBooleanWidget()
    )
    OE = fields.Field(attribute="OE", widget=resource_widget.CharWidget())
    RF = fields.Field(attribute="RF", widget=widgets.CustomBooleanWidget())
    SL = fields.Field(attribute="SL", widget=widgets.CustomBooleanWidget())
    taksit_active = fields.Field(
        column_name="Taksit active",
        attribute="taksit_active",
        widget=widgets.CustomBooleanWidget()
    )
    
    taksit_2 = fields.Field(
        column_name="Taksit 2 ay",
        attribute="taksit_2",
        widget=widgets.CustomDecimalWidget(2),
    )
    taksit_2_active = fields.Field(
        column_name="Taksit 2 active",
        attribute="taksit_2_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_3 = fields.Field(
        column_name="Taksit 3 ay",
        attribute="taksit_3",
        widget=widgets.CustomDecimalWidget(3),
    )
    taksit_3_active = fields.Field(
        column_name="Taksit 3 active",
        attribute="taksit_3_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_6 = fields.Field(
        column_name="Taksit 6 ay",
        attribute="taksit_6",
        widget=widgets.CustomDecimalWidget(6),
    )
    taksit_6_active = fields.Field(
        column_name="Taksit 6 active",
        attribute="taksit_6_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_9 = fields.Field(
        column_name="Taksit 9 ay",
        attribute="taksit_9",
        widget=widgets.CustomDecimalWidget(9),
    )
    taksit_9_active = fields.Field(
        column_name="Taksit 9 active",
        attribute="taksit_9_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_12 = fields.Field(
        column_name="Taksit 12 ay",
        attribute="taksit_12",
        widget=widgets.CustomDecimalWidget(12),
    )
    taksit_12_active = fields.Field(
        column_name="Taksit 12 active",
        attribute="taksit_12_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_active = fields.Field(
        column_name="Kredit active",
        attribute="kredit_active",
        widget=widgets.CustomBooleanWidget()
    )
    taksit_active = fields.Field(
        column_name="Taksit active",
        attribute="taksit_active",
        widget=widgets.CustomBooleanWidget()
    )
    kredit_3 = fields.Field(
        column_name="Kredit 3 ay",
        attribute="kredit_3",
        widget=widgets.CustomDecimalWidget(3),
    )
    kredit_3_active = fields.Field(
        column_name="Kredit 3 active",
        attribute="kredit_3_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_3_dif = fields.Field(
        column_name="Bahalaşma 3 %",
        attribute="kredit_3_dif",
        widget=widgets.DecimalWidget(),
    )

    kredit_6 = fields.Field(
        column_name="Kredit 6 ay",
        attribute="kredit_6",
        widget=widgets.CustomDecimalWidget(6),
    )
    kredit_6_active = fields.Field(
        column_name="Kredit 6 active",
        attribute="kredit_6_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_6_dif = fields.Field(
        column_name="Bahalaşma 6 %",
        attribute="kredit_6_dif",
        widget=widgets.DecimalWidget(),
    )

    kredit_9 = fields.Field(
        column_name="Kredit 9 ay",
        attribute="kredit_9",
        widget=widgets.CustomDecimalWidget(9),
    )
    kredit_9_active = fields.Field(
        column_name="Kredit 9 active",
        attribute="kredit_9_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_9_dif = fields.Field(
        column_name="Bahalaşma 9 %",
        attribute="kredit_9_dif",
        widget=widgets.DecimalWidget(),
    )

    kredit_12 = fields.Field(
        column_name="Kredit 12 ay",
        attribute="kredit_12",
        widget=widgets.CustomDecimalWidget(12),
    )
    kredit_12_active = fields.Field(
        column_name="Kredit 12 active",
        attribute="kredit_12_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_12_dif = fields.Field(
        column_name="Bahalaşma 12 %",
        attribute="kredit_12_dif",
        widget=widgets.DecimalWidget(),
    )

    USDNO = fields.Field(
        column_name="price", attribute="USDNO", widget=resource_widget.DecimalWidget()
    )
    USD = fields.Field(
        column_name="sale", attribute="USD", widget=resource_widget.DecimalWidget()
    )
    USD_active = fields.Field(
        column_name="sale active",
        attribute="USD_active",
        widget=widgets.CustomBooleanWidget()
    )

    USDOFF = fields.Field(
        column_name="Price Difference",
        attribute="USDOFF",
        widget=resource_widget.DecimalWidget(),
    )

    montaj_balance = fields.Field(
        column_name="Montaj+Balance",
        attribute="montaj_balance",
        widget=resource_widget.DecimalWidget(),
    )
    Class = fields.Field(
        column_name="class", attribute="Class", widget=widgets.CustomClassWidget()
    )

    size = fields.Field(attribute="size", widget=widgets.CustomSizeWidget())
    release_date = fields.Field(
        attribute="release_date",
        widget=resource_widget.CharWidget()
    )

    db= fields.Field(attribute="db",widget=resource_widget.IntegerWidget())
    fuel = fields.Field(attribute="fuel",widget=resource_widget.CharWidget())
    contact = fields.Field(attribute="contact",widget=resource_widget.CharWidget())

    class Meta:
        model = Tire
        fields = (
            "id",
            "brand",
            "serie",
            "manufacturer",
            "size",
            "ZR",
            "MS",
            "OE",
            "SL",
            "RF",
            "tradeware",
            "weight",
            "speed",
            "razval",
            "year",
            "Class",
            "quantity",
            "kredit_active",
            "kredit_12_dif",
            "kredit_9_dif",
            "kredit_6_dif",
            "kredit_3_dif",
            "kredit_3",
            "kredit_3_active",
            "kredit_6",
            "kredit_6_active",
            "kredit_9",
            "kredit_9_active",
            "kredit_12",
            "kredit_12_active",
            "taksit_active",
            "taksit_2",
            "taksit_2_active",
            "taksit_3",
            "taksit_3_active",
            "taksit_6",
            "taksit_6_active",
            "taksit_9",
            "taksit_9_active",
            "taksit_12",
            "taksit_12_active",
            "USDNO",
            "USD",
            "USD_active",
            "USDOFF",
            "release_date",
            "db",
            "fuel",
            "contact"
        )
        skip_unchanged = True

        export_order = (
            "id",
            "brand",
            "serie",
            "origin",
            "manufacturer",
            "size",
            "ZR",
            "MS",
            "OE",
            "SL",
            "RF",
            "season",
            "tradeware",
            "weight",
            "speed",
            'db',
            "fuel",
            "contact",
            "USDNO",
            "USD",
            "USD_active",
            "USDOFF",
            "montaj_balance",
            "razval",
            "year",
            "Class",
            "taksit_active",
            "taksit_2",
            "taksit_2_active",
            "taksit_3",
            "taksit_3_active",
            "taksit_6",
            "taksit_6_active",
            "taksit_9",
            "taksit_9_active",
            "taksit_12",
            "taksit_12_active",
            "kredit_active",
            "kredit_3",
            "kredit_3_dif",
            "kredit_3_active",
            "kredit_6",
            "kredit_6_dif",
            "kredit_6_active",
            "kredit_9",
            "kredit_9_dif",
            "kredit_9_active",
            "kredit_12",
            "kredit_12_dif",
            "kredit_12_active",
            "quantity",
            "release_date"
        )
