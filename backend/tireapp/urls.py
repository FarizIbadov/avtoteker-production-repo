from django.urls import path, include
from . import views

urlpatterns = [
    path("tires/", views.TireListView.as_view(), name="list"),
    path("tires/<str:width>-<str:height>-<str:radius>/", views.TireListView.as_view(), name="detail-list"),
    path("tires/<int:pk>/<str:slug>/", views.TireDetailView.as_view(), name="detail"),
]
