class FilterBySizeMixin:
    def get_filter(self):
        field_to_model = {
            "width": "size__width",
            "height": "size__height",
            "radius": "size__radius",
        }
        kwargs = {}
        

        for key, value in field_to_model.items():
            if self.kwargs.get(key, "_") != "_":
                kwargs[value] = self.kwargs[key] if self.kwargs[key] != '-' else ""

        return kwargs
