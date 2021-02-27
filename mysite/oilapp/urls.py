from django.urls import path
from .views import OilMainView,OilListView

urlpatterns = [
    path("oil/",OilMainView.as_view(),name="oil"),
    path("oil-list/",OilListView.as_view(),name="oil-list")
]

