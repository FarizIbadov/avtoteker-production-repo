from django.contrib.sitemaps import Sitemap
from tireapp.models import Tire
from oilapp.models import Oil

class TireSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "http"

    def items(self):
        return Tire.objects.all()

class OilSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "http" 

    def items(self):
        return Oil.objects.all()