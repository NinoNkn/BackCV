# urls.py
from django.urls import path
from .views import RecetaListView

urlpatterns = [
    path("recetas/", RecetaListView.as_view(), name="recetas-list"),
]
