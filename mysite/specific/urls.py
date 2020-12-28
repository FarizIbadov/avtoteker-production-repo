from django.urls import path, include
from .views import (
    AdminSpecificListView,
    AdminSpecificDetailView,
    AdminSpecificCreateView,
    AdminSpecificUpdateView,
    AdminSpecificDeleteView,
)


app_name = "specific"
urlpatterns = [
    path("country/", AdminSpecificListView.as_view(), name="country"),
    path("brand/", AdminSpecificListView.as_view(), name="brand"),
    path("serie/", AdminSpecificListView.as_view(), name="serie"),
    path("season/", AdminSpecificListView.as_view(), name="season"),
    path("country/add/", AdminSpecificCreateView.as_view(), name="country-add"),
    path("brand/add/", AdminSpecificCreateView.as_view(), name="brand-add"),
    path("serie/add/", AdminSpecificCreateView.as_view(), name="serie-add"),
    path("season/add/", AdminSpecificCreateView.as_view(), name="season-add"),
    path("country/<int:pk>/", AdminSpecificDetailView.as_view(), name="country-detail"),
    path("brand/<int:pk>/", AdminSpecificDetailView.as_view(), name="brand-detail"),
    path("serie/<int:pk>/", AdminSpecificDetailView.as_view(), name="serie-detail"),
    path("season/<int:pk>/", AdminSpecificDetailView.as_view(), name="season-detail"),
    path(
        "country/<int:pk>/update/",
        AdminSpecificUpdateView.as_view(),
        name="country-update",
    ),
    path(
        "brand/<int:pk>/update/", AdminSpecificUpdateView.as_view(), name="brand-update"
    ),
    path(
        "serie/<int:pk>/update/", AdminSpecificUpdateView.as_view(), name="serie-update"
    ),
    path(
        "season/<int:pk>/update/",
        AdminSpecificUpdateView.as_view(),
        name="season-update",
    ),
    path(
        "country/<int:pk>/delete/",
        AdminSpecificDeleteView.as_view(),
        name="country-delete",
    ),
    path(
        "brand/<int:pk>/delete/", AdminSpecificDeleteView.as_view(), name="brand-delete"
    ),
    path(
        "serie/<int:pk>/delete/", AdminSpecificDeleteView.as_view(), name="serie-delete"
    ),
    path(
        "season/<int:pk>/delete/",
        AdminSpecificDeleteView.as_view(),
        name="season-delete",
    ),
]
