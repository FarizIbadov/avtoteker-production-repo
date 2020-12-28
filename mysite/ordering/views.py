from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import OrderForm


class OrderCreateView(CreateView):
    form_class = OrderForm

    def get_success_url(self):
        return reverse('list')

    def form_invalid(self,form):
        return redirect('home')
