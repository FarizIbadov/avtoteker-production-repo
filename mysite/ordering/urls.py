from django.urls import path
from .views import OilOrderAPIView,TireOrderAPIView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("tire/",TireOrderAPIView.as_view(),name="tire-order"),
    path("oil/",OilOrderAPIView.as_view(),name="oil-order"),
]
