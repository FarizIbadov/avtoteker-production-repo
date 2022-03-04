from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib.postgres.search import TrigramSimilarity
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView,View
from .mixins import FilterBySizeMixin
from tireapp.models import Tire
from specific.models import Brand,Serie
from ordering.forms import OrderForm
import re


class MainPage(TemplateView):
    template_name = "main_site/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context


class MainListView(FilterBySizeMixin, ListView):
    paginate_by = 8
    template_name = "tire/list.html"

    def get_queryset(self):        
        kwargs = self.get_filter()
        queryset = Tire.objects.available(**kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Seçim edin")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context


class MainDetailView(DetailView):
    model = Tire
    template_name = "tire/detail.html"
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Seçim edin")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context
        