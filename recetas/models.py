from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=300)
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=200)
    imagen_url = models.URLField(max_length=500)

    def __str__(self):
        return self.titulo
