from django.views.generic import ListView,DetailView
from .models import News

class NewsListView(ListView):
    template_name = "main_site/news-list.html"
    paginate_by = 8

    def get_queryset(self,*args,**kwargs):
        return News.objects.filter(active=True).order_by('order')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context

class NewsDetailView(DetailView):
    template_name = "main_site/news-detail.html"
    model = News

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context
    