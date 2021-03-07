from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import OrderForm,OilOrderForm

class OrderCreateView(CreateView):
    form_class = OrderForm

    def get_success_url(self):
        return reverse('list')

    def form_invalid(self,form):
        return redirect('home')

class OilOrderCreateView(CreateView):
    form_class = OilOrderForm

    def get_success_url(self):
        return reverse('oil-list')

    def form_invalid(self,form):
        return redirect('oil')
