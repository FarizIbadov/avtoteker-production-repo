from django.urls import path
from .views import KreditListView,KreditDetailView

urlpatterns = [
    path("",KreditListView.as_view(),name="kredit-list"),
    path("<slug:slug>/",KreditDetailView.as_view(),name="kredit-detail"),
]