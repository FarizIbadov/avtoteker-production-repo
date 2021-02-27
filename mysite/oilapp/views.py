from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Oil

class OilMainView(TemplateView):
    template_name = "main_site/oil-main.html"

class OilListView(ListView):
    template_name = "main_site/oil-list.html"

    def get_queryset(self,*args,**kwargs):
        return Oil.objects.filter()