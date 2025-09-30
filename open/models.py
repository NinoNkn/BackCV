# models.py
from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=300)
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=300)
    imagen = models.URLField()  # o ImageField si manejas media en tu CMS

    def __str__(self):
        return self.titulo
