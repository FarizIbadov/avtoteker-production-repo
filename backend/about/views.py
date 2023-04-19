from django.views.generic import TemplateView
from django.utils.translation import gettext as _ 
from . import models

class AboutView(TemplateView):
    template_name = "main_site/about.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['about'] = models.About.objects.filter(active=True).first()
        title = _("Seçim edin")
        context['tire_search_title'] = f"""<h2 class='tire-search__heading'>{title}</h2>"""
        return context
