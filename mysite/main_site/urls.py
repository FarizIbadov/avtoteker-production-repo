from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .views import MainPage, MainListView, MainDetailView
from .sitemaps import TireSitemap

sitemaps = {
    'tires': TireSitemap
}

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("sitemap.xml",sitemap,{"sitemaps":sitemaps}),
    path("tires/", MainListView.as_view(), name="list"),
    path("tires/<int:pk>/", MainDetailView.as_view(), name="detail"),
    path('order/',include('ordering.urls'))
]
