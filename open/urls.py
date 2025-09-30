from django.urls import path
from .views import RecetaListCreateView

urlpatterns = [
    path('', RecetaListCreateView.as_view(), name='receta-list'),
]
