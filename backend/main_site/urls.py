from django.urls import path,re_path ,include
from django.contrib.sitemaps.views import sitemap
from .views import MainPage
from .sitemaps import TireSitemap,OilSitemap

sitemaps = {
    'tires': TireSitemap,
    "oil": OilSitemap
}

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("teker-sechimi/", MainPage.as_view(), name="az-home"),
    path("sitemap.xml",sitemap,{"sitemaps":sitemaps}),
]
