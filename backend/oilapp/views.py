from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Oil

class OilMainView(TemplateView):
    template_name = "oil/oil-main.html"

class OilListView(ListView):
    template_name = "oil/oil-list.html"

    def get_queryset(self,*args,**kwargs):
        viscosity = self.request.GET.get("viscosity")
        kwargs = {}
        if viscosity:
            kwargs['viscosity'] = viscosity
        return Oil.objects.available(**kwargs)
        
class OilDetailView(DetailView):
    template_name = "oil/oil-detail.html"

    def get_object(self):
        pk = self.kwargs['pk']
        instance = Oil.objects.get(pk=pk)
        return instance