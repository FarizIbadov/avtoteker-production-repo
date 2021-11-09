class FilterBySizeMixin:
    def get_filter(self):
        field_to_model = {
            "width": "size__width__icontains",
            "height": "size__height__icontains",
            "radius": "size__radius__icontains",
        }
        kwargs = {}
        get_data = self.kwargs

        for key, value in field_to_model.items():
            if get_data.get(key,"_") != "_":
                kwargs[value] = get_data[key] if get_data[key] != '-' else ""
            else:
                continue


        return {**kwargs}
