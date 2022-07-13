from django.shortcuts import render
from django.views.generic import TemplateView

from . import models

class CartView(TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = models.Cart.objects.get_cart(self.request)
        return context