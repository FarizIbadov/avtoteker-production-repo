from django.urls import path
from . import views 

urlpatterns = [
    path("",views.MainContentView.as_view(),name="about-us")
]