from import_export import resources,fields
from tireapp import widgets as tire_widgets
from . import widgets
from .models import Oil

class OilResource(resources.ModelResource):
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
            models = self.Meta.model.objects.all().exclude(id__in=filtered_ids)
            models.delete()
            
    brand = fields.Field(
        attribute="brand",
        widget=widgets.CustomBrandWidget()
    )

    serie = fields.Field(
        attribute="serie",
        widget=widgets.CustomSerieWidget()
    )
    
    country = fields.Field(
        attribute="country",
        widget=tire_widgets.CustomCountryWidget()
    )

    cost = fields.Field(
        column_name="cost",
        attribute="cost",
        widget=tire_widgets.CustomBooleanWidget()
    )

    taksit_active = fields.Field(
        column_name="Taksit active",
        attribute="taksit_active",
        widget=tire_widgets.CustomBooleanWidget()
    )

    taksit_2 = fields.Field(
        column_name="Taksit 2 ay",
        attribute="taksit_2",
        widget=tire_widgets.CustomFloatWidget(2),
    )
    taksit_2_active = fields.Field(
        column_name="Taksit 2 active",
        attribute="taksit_2_active",
        widget=tire_widgets.CustomBooleanWidget(),
    )
    taksit_3 = fields.Field(
        column_name="Taksit 3 ay",
        attribute="taksit_3",
        widget=tire_widgets.CustomFloatWidget(3),
    )
    taksit_3_active = fields.Field(
        column_name="Taksit 3 active",
        attribute="taksit_3_active",
        widget=tire_widgets.CustomBooleanWidget(),
    )
    taksit_6 = fields.Field(
        column_name="Taksit 6 ay",
        attribute="taksit_6",
        widget=tire_widgets.CustomFloatWidget(6),
    )
    taksit_6_active = fields.Field(
        column_name="Taksit 6 active",
        attribute="taksit_6_active",
        widget=tire_widgets.CustomBooleanWidget(),
    )
    taksit_9 = fields.Field(
        column_name="Taksit 9 ay",
        attribute="taksit_9",
        widget=tire_widgets.CustomFloatWidget(9),
    )
    taksit_9_active = fields.Field(
        column_name="Taksit 9 active",
        attribute="taksit_9_active",
        widget=tire_widgets.CustomBooleanWidget(),
    )
    taksit_12 = fields.Field(
        column_name="Taksit 12 ay",
        attribute="taksit_12",
        widget=tire_widgets.CustomFloatWidget(12),
    )
    taksit_12_active = fields.Field(
        column_name="Taksit 12 active",
        attribute="taksit_12_active",
        widget=tire_widgets.CustomBooleanWidget(),
    )

    class Meta:
        model = Oil
        fields = (
            "id",
            "brand",
            "serie",
            "volume",
            "viscosity",
            "fuel",
            "country",
            "oil_type",
            "image_url",
            "des1",
            "description",
            "price",
            "sale",
            "cost",
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
            'stickers',
            "campaigns"
        )

        skip_unchanged = True

        export_order = (
            "id",
            "brand",
            "serie",
            "volume",
            "viscosity",
            "fuel",
            "country",
            "oil_type",
            "image_url",
            "des1",
            "description",
            "price",
            "sale",
            "cost",
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
        )