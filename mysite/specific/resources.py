from import_export import resources, fields
from import_export import widgets as resource_widget
from . import widgets
from .models import Serie

class SerieResource(resources.ModelResource):
    def get_queryset(self):
        return self.Meta.model.objects.all().order_by("id")

    title = fields.Field(attribute='title',widget=resource_widget.CharWidget())
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