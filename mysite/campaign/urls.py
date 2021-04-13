from django.urls import path
from .views import CampaignListView,CampaignDetailView

urlpatterns = [
    path("campaigns/",CampaignListView.as_view(),name="campaign-list"),
    path("campaigns/<int:pk>/",CampaignDetailView.as_view(),name="campaign-detail"),
]