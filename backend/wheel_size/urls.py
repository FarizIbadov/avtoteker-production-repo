from django.urls import path
from .api import MakeListAPIView,ModelListAPIView,YearListAPIView,TrimListAPIView
from .views import TireSizeView

urlpatterns = [
    path("api/makes/", MakeListAPIView.as_view(), name="api-makes"),
    path("api/models/", ModelListAPIView.as_view(), name="api-models"),
    path("api/years/", YearListAPIView.as_view(), name="api-years"),
    path("api/trims/", TrimListAPIView.as_view(), name="api-trims"),
    path("search/",TireSizeView.as_view(),name="search")
]
