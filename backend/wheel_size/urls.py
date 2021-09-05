from django.urls import path
from .api import MakeListAPIView,ModelListAPIView,YearListAPIView,TrimListAPIView
from .views import TireSizeView

urlpatterns = [
    path("api/makes/", MakeListAPIView.as_view()),
    path("api/models/", ModelListAPIView.as_view()),
    path("api/years/", YearListAPIView.as_view()),
    path("api/trims/", TrimListAPIView.as_view()),
    path("search/",TireSizeView.as_view(),name="search")
]
