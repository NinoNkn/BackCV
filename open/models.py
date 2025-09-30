# models.py
from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=250)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo
