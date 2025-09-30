from django.http import JsonResponse
from .models import Receta

def recetas_api(request):
    recetas = list(
        Receta.objects.values(
            "id",
            "titulo",
            "resumen",
            "descripcion",
            "imagen_url",
            "palabras_clave"
        )
    )
    return JsonResponse({"recetas": recetas})
