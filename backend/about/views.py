from django.views.generic import TemplateView
from . import models

class AboutView(TemplateView):
    template_name = "main_site/about.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['about'] = models.About.objects.filter(active=True).first()
        return context
