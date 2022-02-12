from import_export import resources, fields
from import_export import widgets as resource_widget
from .models import Tire, OsTireImporterSetting
from . import widgets
from .utils import generate_trim_code

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

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.generate_trim_code()
        instance.generate_slug()



    id = fields.Field(
        attribute="id",
        widget=resource_widget.IntegerWidget()
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
        widget=widgets.CustomFloatWidget(2),
    )
    taksit_2_active = fields.Field(
        column_name="Taksit 2 active",
        attribute="taksit_2_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_3 = fields.Field(
        column_name="Taksit 3 ay",
        attribute="taksit_3",
        widget=widgets.CustomFloatWidget(3),
    )
    taksit_3_active = fields.Field(
        column_name="Taksit 3 active",
        attribute="taksit_3_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_6 = fields.Field(
        column_name="Taksit 6 ay",
        attribute="taksit_6",
        widget=widgets.CustomFloatWidget(6),
    )
    taksit_6_active = fields.Field(
        column_name="Taksit 6 active",
        attribute="taksit_6_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_9 = fields.Field(
        column_name="Taksit 9 ay",
        attribute="taksit_9",
        widget=widgets.CustomFloatWidget(9),
    )
    taksit_9_active = fields.Field(
        column_name="Taksit 9 active",
        attribute="taksit_9_active",
        widget=widgets.CustomBooleanWidget(),
    )
    taksit_12 = fields.Field(
        column_name="Taksit 12 ay",
        attribute="taksit_12",
        widget=widgets.CustomFloatWidget(12),
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
        widget=widgets.CustomFloatWidget(3),
    )
    kredit_3_active = fields.Field(
        column_name="Kredit 3 active",
        attribute="kredit_3_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_3_dif = fields.Field(
        column_name="Bahalaşma 3 %",
        attribute="kredit_3_dif",
        widget=widgets.FloatWidget(),
    )

    kredit_6 = fields.Field(
        column_name="Kredit 6 ay",
        attribute="kredit_6",
        widget=widgets.CustomFloatWidget(6),
    )
    kredit_6_active = fields.Field(
        column_name="Kredit 6 active",
        attribute="kredit_6_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_6_dif = fields.Field(
        column_name="Bahalaşma 6 %",
        attribute="kredit_6_dif",
        widget=widgets.FloatWidget(),
    )

    kredit_9 = fields.Field(
        column_name="Kredit 9 ay",
        attribute="kredit_9",
        widget=widgets.CustomFloatWidget(9),
    )
    kredit_9_active = fields.Field(
        column_name="Kredit 9 active",
        attribute="kredit_9_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_9_dif = fields.Field(
        column_name="Bahalaşma 9 %",
        attribute="kredit_9_dif",
        widget=widgets.FloatWidget(),
    )

    kredit_12 = fields.Field(
        column_name="Kredit 12 ay",
        attribute="kredit_12",
        widget=widgets.CustomFloatWidget(12),
    )
    kredit_12_active = fields.Field(
        column_name="Kredit 12 active",
        attribute="kredit_12_active",
        widget=widgets.CustomBooleanWidget(),
    )
    kredit_12_dif = fields.Field(
        column_name="Bahalaşma 12 %",
        attribute="kredit_12_dif",
        widget=widgets.FloatWidget(),
    )

    price = fields.Field(
        column_name="price", attribute="price", widget=resource_widget.FloatWidget()
    )
    sale = fields.Field(
        column_name="sale", attribute="sale", widget=resource_widget.FloatWidget()
    )
    cost = fields.Field(
        column_name="cost",
        attribute="cost",
        widget=resource_widget.FloatWidget()
    )

    montaj_balance = fields.Field(
        column_name="Montaj+Balance",
        attribute="montaj_balance",
        widget=resource_widget.FloatWidget(),
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

    kredit_3_month_price = fields.Field(
        column_name="kredit 3 month price %",
        attribute="kredit_3_month_price",
        widget=resource_widget.FloatWidget()
    )
    
    kredit_6_month_price = fields.Field(
        column_name="kredit 6 month price %",
        attribute="kredit_6_month_price",
        widget=resource_widget.FloatWidget()
    )

    new = fields.Field(attribute="new",widget=widgets.CustomNewBooleanWidget())
    outlet = fields.Field(attribute="outlet",widget=widgets.CustomOutletBooleanWidget())

    class Meta:
        model = Tire
        import_id_fields = ("id",)

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
            "cost",
            "price_3",
            "release_date",
            "db",
            "fuel",
            "contact",
            "kredit_3_month_price",
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
        batch_size = 500

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
            "cost",
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
            "kredit_3_month_price",
            "kredit_6",
            "kredit_6_dif",
            "kredit_6_active",
            "kredit_6_month_price",
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
        self.quantity_field = "Miqdar"

        if setting:
            self.code_field = setting.look_up
            self.quantity_field = setting.get_from_field
            

    def process_import(self):
        for row in self.dataset.dict:
            code = row.get(self.code_field)
            quantity = int(row.get(self.quantity_field) or 0)
        
            if not code:
                continue

            self.codes.append(code)
            self.process_tire(code, quantity)

        self.codes.append("XXX")
    

    def get_tire(self, code):
        self.row_is_included = False
        trim_code = generate_trim_code(code)
        filtered_tire = list(filter(self.filter_tire(trim_code), self.updated_tires))
       
        if filtered_tire:
            return filtered_tire[0]   
        return self.tires.filter(trim_code=trim_code).first()

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

        Tire.objects.bulk_update(self.updated_tires, batch_size=500, fields=['quantity'])
        Tire.objects.filter(pk__in=self.deleted_tires).delete()


    def filter_tire(self, code):
        def _filter_tire(value):
            if code == value.trim_code:
                self.row_is_included = True
            return code == value.trim_code
        return _filter_tire

