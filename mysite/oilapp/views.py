from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Oil
from ordering.forms import OilOrderForm

class OilMainView(TemplateView):
    template_name = "main_site/oil-main.html"

class OilListView(ListView):
    paginate_by = 8
    template_name = "main_site/oil-list.html"

    def get_queryset(self,*args,**kwargs):
        viscosity = self.request.GET.get("viscosity")
        kwargs = {}
        if viscosity:
            kwargs['viscosity'] = viscosity
        return Oil.objects.available(**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OilOrderForm
        return context

class OilDetailView(DetailView):
    template_name = "main_site/oil-detail.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OilOrderForm
        
        return context

    def get_object(self):
        pk = self.kwargs['pk']
        instance = Oil.objects.get(pk=pk)
        return instance
    