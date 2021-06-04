from import_export.instance_loaders import ModelInstanceLoader

class CustomModelInstanceLoader(ModelInstanceLoader):
    def get_instance(self, row):
        try:
            params = {}
            for key in self.resource.get_import_id_fields():
                field = self.resource.fields[key]
                params[field.attribute] = field.clean(row)
            if params:
                print(self.get_queryset().filter(**params).first())
                return self.get_queryset().filter(**params).first()
            else:
                return None
        except self.resource._meta.model.DoesNotExist:
            return None