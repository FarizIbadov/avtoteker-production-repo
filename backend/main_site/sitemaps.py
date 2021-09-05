from django.contrib.sitemaps import Sitemap
from secure_sites.models import SecureSite
from tireapp.models import Tire
from oilapp.models import Oil

class SecureSitemap(Sitemap):
    def get_urls(self, page=1, site=None, protocol=None):
        secure_site = SecureSite.objects.filter(active=True).first()
        protocol = secure_site.get_protocol() 
        site = secure_site.site
        urls = super().get_urls(page, site=site, protocol=protocol) 
        return urls


class TireSitemap(SecureSitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Tire.objects.all()

class OilSitemap(SecureSitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Oil.objects.all()