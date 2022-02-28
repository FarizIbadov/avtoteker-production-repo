class FilterBySizeMixin:
    def get_filter(self):
        field_to_model = {
            "width": "size__width__icontains",
            "height": "size__height__icontains",
            "radius": "size__radius__icontains",
        }
        kwargs = {}
   

        for key, value in field_to_model.items():
            if self.kwargs.get(key, "_") != "_":
                kwargs[value] = self.kwargs[key] if self.kwargs[key] != '-' else ""
            else:
                continue

        return {**kwargs}
