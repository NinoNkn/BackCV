# serializers.py
from rest_framework import serializers
from .models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ["id", "titulo", "resumen", "descripcion", "palabras_clave", "imagen"]
