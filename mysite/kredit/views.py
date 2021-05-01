from django.shortcuts import redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import ModelFormMixin 
from .models import Kredit

class KreditListView(ListView):
    template_name = "main_site/kredit-list.html"

    def get_queryset(self,*args,**kwargs):
        return Kredit.objects.available()

    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context

class KreditDetailView(ModelFormMixin,DetailView):
    template_name = "main_site/kredit.html"
    fields = "__all__"
    model = Kredit
    success_url = ""

    def get_form_class(self):
        print(self.kwargs['slug'])
        return super().get_form_class()

    def post(self,request,*args,**kwargs):
        return redirect('kredit-list')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context 