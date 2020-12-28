from django.urls import path, include
from .views import AdminLogin, AdminLogout


app_name = "custom-admin"
urlpatterns = [
    path("", include("tireapp.urls")),
    path("", include("specific.urls")),
    path("login/", AdminLogin.as_view(), name="login"),
    path("logout/", AdminLogout.as_view(), name="logout"),
]
