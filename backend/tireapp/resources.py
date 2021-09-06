from import_export import resources, fields
from import_export import widgets as resource_widget
from .models import Tire, OsTireImporterSetting
from . import widgets

import tablib

class TireResource(resources.ModelResource):
    def get_queryset(self):
        return Tire.objects.all()
    
    def export(self,queryset,*args,**kwargs):
        tires = Tire.objects.available()
        return super().export(tires,*args,**kwargs)

    def before_import(self,dataset, using_transactions, dry_run, **kwargs):
        imported_ids = []
        if not dry_run:
            for row in dataset:
                imported_ids.append(row[0])

            filtered_ids = list(filter(None,imported_ids))
            tires = Tire.objects.all()
            tires.backup()
            tires.exclude(id__in=filtered_ids).delete()

    

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

    price = fields.Field(
        column_name="price", attribute="price", widget=resource_widget.DecimalWidget()
    )
    sale = fields.Field(
        column_name="sale", attribute="sale", widget=resource_widget.DecimalWidget()
    )
    sale_active = fields.Field(
        column_name="sale active",
        attribute="sale_active",
        widget=widgets.CustomBooleanWidget()
    )

    montaj_balance = fields.Field(
        column_name="Montaj+Balance",
        attribute="montaj_balance",
        widget=resource_widget.DecimalWidget(),
    )
    tire_class = fields.Field(
        column_name="class", attribute="tire_class", widget=widgets.CustomClassWidget()
    )

    size = fields.Field(attribute="size", widget=widgets.CustomSizeWidget())
    release_date = fields.Field(
        attribute="release_date",
        widget=resource_widget.CharWidget()
    )

    db= fields.Field(attribute="db",widget=resource_widget.IntegerWidget())
    fuel = fields.Field(attribute="fuel",widget=resource_widget.CharWidget())
    contact = fields.Field(attribute="contact",widget=resource_widget.CharWidget())
    kredit_initial_price = fields.Field(column_name="kredit initial price %",attribute="kredit_initial_price",widget=resource_widget.FloatWidget())
    new = fields.Field(attribute="new",widget=widgets.CustomNewBooleanWidget())
    outlet = fields.Field(attribute="outlet",widget=widgets.CustomOutletBooleanWidget())

    class Meta:
        model = Tire
        import_id_fields = ("id",'code')

        fields = (
            "id",
            "code",
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
            "price",
            "sale",
            "sale_active",
            "price_3",
            "release_date",
            "db",
            "fuel",
            "contact",
            "kredit_initial_price",
            "new",
            "outlet",
            "birkart",
            "tamkart",
            "bolkart",
            "albalikart",
            "kredit",
            "stickers",
            'campaigns'
        )
        skip_unchanged = True
        use_bulk = True

        export_order = (
            "id",
            "code",
            "brand",
            "serie",
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
            "price",
            "sale",
            "sale_active",
            "price_3",
            "montaj_balance",
            "razval",
            "year",
            "tire_class",
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
            "kredit_initial_price",
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
            "release_date",
            "new",
            "outlet"
        )



class OsTireImporter:
    def __init__(self, dataset: tablib.Dataset):
        self.tires = Tire.objects.available()
        self.updated_tires = []
        self.deleted_tires = []
        self.codes = []
        self.dataset = dataset
        self.row_is_included = False

        self.init_settings()

    def init_settings(self):
        setting = OsTireImporterSetting.objects.filter(active=True).first()
        self.code_field = "Mal"
        self.quantity_field = "Cəmi"

        if setting:
            self.code_field = setting.look_up
            self.quantity_field = setting.get_from_field

    def process_import(self):
        for row in self.dataset.dict:
            code = row.get(self.code_field)
            quantity = int(row.get(self.quantity_field, 0))
            
            if not code:
                continue

            self.codes.append(code)
            self.process_tire(code, quantity)

        self.codes.append("XXX")
    

    def get_tire(self, code):
        self.row_is_included = False
        filtered_tire = list(filter(self.filter_tire(code),self.updated_tires))
       
        if filtered_tire:
            return filtered_tire[0]   
        return self.tires.filter(code=code).first()

    def process_tire(self, code, quantity):
        tire = self.get_tire(code)
        if not tire:
            return

        if quantity <= 0:
            self.deleted_tires.append(tire.pk)
        else:
            tire.quantity = quantity

        if not self.row_is_included:
            self.updated_tires.append(tire)

    def process_save(self):
        codes = list(set(filter(None,self.codes)))
        Tire.objects.exclude(code__in=codes).delete()

        Tire.objects.bulk_update(self.updated_tires, batch_size=1000, fields=['quantity'])
        Tire.objects.filter(pk__in=self.deleted_tires).delete()


    def filter_tire(self, code):
        def _filter_tire(value):
            if code == value.code:
                self.row_is_included = True
            return code == value.code
        return _filter_tire
