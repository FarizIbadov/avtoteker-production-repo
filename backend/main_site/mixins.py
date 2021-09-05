class FilterBySizeMixin:
    def get_filter(self):
        field_to_model = {
            "width": "size__width",
            "height": "size__height",
            "radius": "size__radius",
        }
        kwargs = {}
        get_data = self.kwargs

        for key, value in field_to_model.items():
            if get_data.get(key,"_") != "_":
                kwargs[value] = get_data[key]
            else:
                continue


        return {**kwargs}
