class FilterBySizeMixin:
    def get_filter(self):
        field_to_model = {
            "width": "size__width",
            "height": "size__height",
            "radius": "size__radius",
            "brand": "brand__title__icontains",
            "serie": "serie__title__icontains"
        }
        kwargs = {}
        get_data = self.request.GET

        for key, value in field_to_model.items():
            if get_data.get(key):
                kwargs[value] = get_data[key]
            else:
                continue

        return {**kwargs}
