from django.views.generic import ListView,DetailView
from .models import Post

class CampaignListView(ListView):
    template_name = "main_site/campaign-list.html"
    paginate_by = 8

    def get_queryset(self,*args,**kwargs):
        return Post.objects.filter(active=True).order_by('order')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context

class CampaignDetailView(DetailView):
    template_name = "main_site/campaign-detail.html"
    model = Post

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='h2 tire-search__heading'>Təkər seçimi</h2>"
        return context
    