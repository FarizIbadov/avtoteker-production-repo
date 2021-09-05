from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView
from app.mixins import IsAdmin
from specific.models import Models
from specific.forms import Forms
from django.urls import resolve, reverse_lazy


class AdminLogin(LoginView):
    template_name = "admin/login.html"
    extra_context = {"title": "Admin - Login"}

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse_lazy("custom-admin:tireapp:home")


class AdminLogout(LogoutView):
    def get_next_page(self):
        return reverse_lazy("custom-admin:login")
