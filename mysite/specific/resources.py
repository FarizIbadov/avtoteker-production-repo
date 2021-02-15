from import_export import resources, fields
from import_export import widgets as resource_widget
from . import widgets
from .models import Serie

class SerieResource(resources.ModelResource):
    def get_queryset(self):
        return self.Meta.model.objects.all().order_by("id")

    def before_import(self,dataset, using_transactions, dry_run, **kwargs):
        imported_ids = []
        if not dry_run:
            for row in dataset:
                imported_ids.append(row[0])
            filtered_ids = list(filter(None,imported_ids))
            prepeared_for_deletion_models = self.Meta.model.objects.all().exclude(id__in=filtered_ids)
            prepeared_for_deletion_models.delete()

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        if not dry_run:
            super().save_instance(instance, using_transactions, dry_run)

    title = fields.Field(attribute='title',widget=widgets.CustomCharWidget())
    brand = fields.Field(attribute="brand",widget=widgets.CustomBrandWidget())
    dry = fields.Field(attribute="dry",widget=resource_widget.IntegerWidget())
    wet = fields.Field(attribute="wet",widget=resource_widget.IntegerWidget())
    offroad = fields.Field(attribute="offroad",widget=resource_widget.IntegerWidget())
    comfort = fields.Field(attribute="comfort",widget=resource_widget.IntegerWidget())
    noise = fields.Field(attribute="noise",widget=resource_widget.IntegerWidget())
    treadware = fields.Field(attribute="treadware",widget=resource_widget.IntegerWidget())
    snow = fields.Field(attribute="snow",widget=resource_widget.IntegerWidget())
    value = fields.Field(attribute="value",widget=resource_widget.IntegerWidget())
    description = fields.Field(attribute="description",widget=resource_widget.CharWidget())
    extra = fields.Field(attribute="extra",widget=resource_widget.CharWidget())
    image_url = fields.Field(attribute="image_url",widget=resource_widget.CharWidget())

    class Meta:
        model = Serie
        fields = (
            "id",
            "title",
            "brand",
            "dry",
            "wet",
            "offroad",
            "comfort",
            "noise",
            "treadware",
            "snow",
            "value",
            "description",
            "extra",
            "image_url"
        )

        skip_unchanged = True

        export_order = (
            "id",
            "title",
            "brand",
            "dry",
            "wet",
            "offroad",
            "comfort",
            "noise",
            "treadware",
            "snow",
            "value",
            "description",
            "extra",
            "image_url"
        )