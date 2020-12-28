from django.urls import path, include
from .views import MainPage, MainListView, MainDetailView

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("tires/", MainListView.as_view(), name="list"),
    path("tires/<int:pk>/", MainDetailView.as_view(), name="detail"),
    path('order/',include('ordering.urls'))
]
