from django.views.generic import TemplateView, ListView, DetailView
from .mixins import FilterBySizeMixin
from tireapp.models import Tire
from ordering.forms import OrderForm


class MainPage(TemplateView):
    template_name = "main_site/index.html"


class MainListView(FilterBySizeMixin, ListView):
    paginate_by = 8
    template_name = "main_site/list.html"

    def get_queryset(self):
        kwargs = self.get_filter()
        return Tire.objects.filter(**kwargs).order_by("-brand__order_number")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm
        return context


class MainDetailView(DetailView):
    template_name = "main_site/detail.html"
    model = Tire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm
        return context
