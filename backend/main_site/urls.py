from django.urls import path,re_path ,include
from django.contrib.sitemaps.views import sitemap
from .views import MainPage, MainListView, MainDetailView
from .sitemaps import TireSitemap,OilSitemap

sitemaps = {
    'tires': TireSitemap,
    "oil": OilSitemap
}

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("sitemap.xml",sitemap,{"sitemaps":sitemaps}),
    path("tires/", MainListView.as_view(), name="list"),
    path("tires/<str:width>-<str:height>-<str:radius>/", MainListView.as_view(), name="detail-list"),
    path("tires/<int:pk>/<str:slug>/", MainDetailView.as_view(), name="detail"),
    # path("search-tire/",MainSearchView.as_view(),name="search-tire"),
]
