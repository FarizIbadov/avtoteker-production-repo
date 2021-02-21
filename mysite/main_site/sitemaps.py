from django.contrib.sitemaps import Sitemap
from tireapp.models import Tire

class TireSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "https"

    def items(self):
        return Tire.objects.all()