from django.urls import path
from django.views.generic import RedirectView

from . import api, views


urlpatterns = [
    path("api/tire-order/",api.TireOrderAPIView.as_view(),name="tire-order"),
    path("api/oil-order/",api.OilOrderAPIView.as_view(),name="oil-order"),

    # path("cart/", views.CartView.as_view(), name="cart-page"),
    # path("cart/order/", RedirectView.as_view(pattern_name="cart-page"))
]
