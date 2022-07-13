from app.mixins import IsAdmin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from specific.models import Models
from app.mixins import GetUrlName, GetFormClass, GetObject


class AdminSpecificListView(IsAdmin, GetUrlName, ListView):
    template_name = "specific/list.html"
    paginate_by = 3

    def get_queryset(self):
        Model = Models[self.get_url_name()]
        return Model.objects.all().order_by("-title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_url_name()
        context["title"] = f"{title.capitalize()}"
        context["add_page"] = reverse_lazy(f"custom-admin:specific:{title}-add")
        return context


class AdminSpecificDetailView(IsAdmin, GetObject, DetailView):
    template_name = "specific/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_url_name()
        detail_title = context["object"].title
        context["title"] = f"{title.capitalize()} - {detail_title}"
        context["is_serie"] = title == "serie"
        context["list_url"] = reverse_lazy(f"custom-admin:specific:{title}")
        return context


class AdminSpecificCreateView(IsAdmin, GetFormClass, CreateView):
    template_name = "specific/form.html"


class AdminSpecificUpdateView(IsAdmin, GetObject, GetFormClass, UpdateView):
    template_name = "specific/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev_page_url"] = reverse_lazy(
            f"custom-admin:specific:{self.get_url_name()}-detail", kwargs=self.kwargs
        )
        return context


class AdminSpecificDeleteView(IsAdmin, GetObject, DeleteView):
    def get_success_url(self):
        return reverse_lazy(f"custom-admin:specific:{self.get_url_name()}")
