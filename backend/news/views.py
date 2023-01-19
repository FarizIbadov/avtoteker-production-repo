from django.views.generic import ListView, DetailView
from .models import News


class NewsListView(ListView):
    template_name = "main_site/news-list.html"
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(active=True).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context


class NewsDetailView(DetailView):
    template_name = "main_site/news-detail.html"
    model = News

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        post = context['object']

        key = self.request.session._SessionBase__session_key

        post.viewed_by.get_or_create(key=key)

        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context
