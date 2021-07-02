from import_export import resources, fields
from import_export import widgets as resource_widget
from .models import Tire,OneSTire
from . import widgets
from .instance_loader import CustomModelInstanceLoader

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
    kredit_initial_price = fields.Field(column_name="kredit initial price %",attribute="kredit_initial_price",widget=resource_widget.FloatWidget())
    new = fields.Field(attribute="new",widget=widgets.CustomNewBooleanWidget())
    outlet = fields.Field(attribute="outlet",widget=widgets.CustomOutletBooleanWidget())

    class Meta:
        model = Tire
        import_id_fields = ("id",'code')
        # instance_loader_class = CustomModelInstanceLoader

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
            "price",
            "sale",
            "sale_active",
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


class OneSTireResource(resources.ModelResource):
    CACHED_QUANTITIES = {}


    code = fields.Field(column_name="Mal",attribute="code")
    price_usd = fields.Field(column_name="Qiymət USD",attribute="price_usd")
    year = fields.Field(column_name="İl",attribute="year")
    country = fields.Field(column_name="Ölkə",attribute="country")
    quantity = fields.Field(column_name="Cəmi",attribute="quantity")   

    def __init__(self):
        super().__init__()
        self.CACHED_QUANTITIES = {}

    def skip_row(self, instance, original):
        if instance.code == "Cəmi":
            return True
        return super().skip_row(instance, original)   

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        try:
            code = row['Mal']
            quantity = row['Cəmi']

            tire = Tire.objects.get(code=code)

            if not quantity:
                tire.delete()
            else: 
                cached_qtn = self.CACHED_QUANTITIES.get(code,0)
                current_qtn = cached_qtn + quantity
                tire.quantity = current_qtn
                tire.save()
                self.CACHED_QUANTITIES[code] = current_qtn
        except Tire.DoesNotExist:
            pass  

    def before_import(self,dataset, using_transactions, dry_run, **kwargs):
        imported_codes = []
        if not dry_run:
            for row in dataset:
                if row[0] != "Cəmi":
                    imported_codes.append(row[0])

                
            filtered_codes = list(filter(None,imported_codes))

            os_tires = OneSTire.objects.exclude(code__in=filtered_codes)
            os_tires.delete()

            tires = Tire.objects.exclude(code="XXX")
            tires.backup()
            tires.exclude(code__in=filtered_codes).delete()

    def for_delete(self,row,instance):
        code = row['Mal']
        if row['Cəmi']:
            if row['Cəmi'] <= 0:
                self.delete_tire(code)
                return True
            return False
        else:
            self.delete_tire(code)
            return True
        
    def import_row(self, row, instance_loader, using_transactions=True, dry_run=False, raise_errors=False, **kwargs):
        row_result = super().import_row(row, instance_loader, using_transactions, dry_run, raise_errors, **kwargs)
        row_result.object_id = row['Mal']
        row_result.object_repr = row['Mal']
        return row_result

    def delete_tire(self,code):
        try:
            tire = Tire.objects.get_object(code=code)
            tire.delete()
        except Tire.DoesNotExist:
            pass
        return
        
    class Meta:
        model = OneSTire 
        fields = ("code","price_usd","year","country","quantity")
        import_id_fields = ('code',)
        use_bulk = True
        # skip_unchanged = True