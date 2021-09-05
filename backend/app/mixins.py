from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy, resolve
from specific.models import Models
from specific.forms import Forms
from django.shortcuts import get_object_or_404


class IsAdmin(LoginRequiredMixin, UserPassesTestMixin):
    def get_login_url(self):
        return reverse_lazy("custom-admin:login")

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class GetUrlName(object):
    def get_url_name(self):
        return str(resolve(self.request.path_info).url_name.split("-")[0])


class GetObject(GetUrlName):
    def get_object(self):
        Model = Models[self.get_url_name()]
        pk = self.kwargs["pk"]
        return get_object_or_404(Model, pk=pk)


class GetFormClass(GetUrlName):
    def get_form_class(self):
        form = Forms[self.get_url_name()]
        return form
