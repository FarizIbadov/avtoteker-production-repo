from django.urls import path
from .views import OrderCreateView,OilOrderCreateView

urlpatterns = [
    path("",OrderCreateView.as_view(),name="order"),
    path("oil/",OilOrderCreateView.as_view(),name="oil-order"),
]
