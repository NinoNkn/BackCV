from django.urls import path
from . import views

urlpatterns = [
    path("api/recetas/", views.recetas_api, name="recetas_api"),
]
