from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "resumen", "palabras_clave")
    search_fields = ("titulo", "palabras_clave")