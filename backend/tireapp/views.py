from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

from .models import Tire
from main_site.mixins import FilterBySizeMixin
from .filters import TireFilter

# class TireWarrantyView(ListView):
#     template_name = "tire/warranty.html"

    # def get_queryset(self):
    #     return TireFilter(self.kwargs, Tire.objects.available()).queryset

    
class TireListView(FilterBySizeMixin,ListView):
    # paginate_by = 8
    template_name = "tire/list.html"

    def get_data(self):
        data = {}

        width = self.kwargs.get('width')
        height = self.kwargs.get('height')
        radius = self.kwargs.get('radius')

        data['width'] = "" if width == "_" else width
        data['height'] = "" if height == "_" else height
        data['radius'] = "" if radius == "_" else radius
        
        return data

    def get_queryset(self):       
        return TireFilter(
            self.get_data(), 
            Tire.objects.available()
        ).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Seçim edin")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context


class TireDetailView(DetailView):
    model = Tire
    template_name = "tire/detail.html"
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Seçim edin")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context