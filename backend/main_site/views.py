from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "main_site/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _("Təkər seçimi")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context



        