from django.urls import path
from . import views

urlpatterns = [
    path(
        "payment/cancel/<str:uuid>/", 
        views.CancelView.as_view(), 
        name="cancel-view"
    ),

    path(
        "payment/<str:uuid>/", 
        views.PaymentView.as_view(), 
        name="payment-view"
    ),

    path(
        "payment/success/<str:uuid>/", 
        views.SuccessView.as_view(), 
        name="success-view"
    ),

   
]