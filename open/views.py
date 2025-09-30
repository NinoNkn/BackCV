# views.py
from rest_framework import generics
from .models import Receta
from .serializers import RecetaSerializer

class RecetaListView(generics.ListAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
