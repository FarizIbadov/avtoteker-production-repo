from django.views.generic import ListView
from .models import Tire

# class TireWarrantyView(FilterBySizeMixin, ListView):
#     def get_queryset(self):
#         kwargs = self.get_filter()
#         queryset = Tire.objects.available(**kwargs)
#         return queryset