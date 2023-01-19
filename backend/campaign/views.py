from django.views.generic import ListView, DetailView
from .models import Post


class CampaignListView(ListView):
    template_name = "main_site/campaign-list.html"
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(active=True).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context


class CampaignDetailView(DetailView):
    template_name = "main_site/campaign-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = context['object']

        key = self.request.session._SessionBase__session_key

        post.viewed_by.get_or_create(key=key)

        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context
