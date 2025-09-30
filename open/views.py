from rest_framework import generics
from .models import Receta
from .serializers import RecetaSerializer

class RecetaListCreateView(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
