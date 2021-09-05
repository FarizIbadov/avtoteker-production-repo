from django.views.generic import ListView
from .models import MainContent


class MainContentView(ListView):
    template_name = "main_site/about-us.html"
    def get_queryset(self):
        return MainContent.objects.filter(active=True)
