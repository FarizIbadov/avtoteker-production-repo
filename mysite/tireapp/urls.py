from django.urls import path, include
from .views import (
    TireListView,
    TireCreateView,
    TireUpdateView,
    TireDetailView,
    TireDeleteView,
    TireExcelView,
)

app_name = "tireapp"
urlpatterns = [
    path("", TireListView.as_view(), name="home"),
    path("tire-excel/", TireExcelView.as_view(), name="excel"),
    path("tire/add/", TireCreateView.as_view(), name="tire-add"),
    path("tire/<int:pk>/", TireDetailView.as_view(), name="tire-detail"),
    path("tire/<int:pk>/update/", TireUpdateView.as_view(), name="tire-update"),
    path("tire/<int:pk>/delete/", TireDeleteView.as_view(), name="tire-delete"),
]
