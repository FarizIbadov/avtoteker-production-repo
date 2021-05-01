from django.urls import path
from .views import NewsDetailView,NewsListView

urlpatterns = [
    path("blogs/",NewsListView.as_view(),name="news-list"),
    path("blogs/<int:pk>/",NewsDetailView.as_view(),name="news-detail"),
]