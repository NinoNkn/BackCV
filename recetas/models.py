from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    descripcion = models.TextField()
    imagen_url = models.URLField("Imagen (URL)", blank=True, null=True)
    palabras_clave = models.CharField(max_length=250, help_text="Separar con comas")

    def __str__(self):
        return self.titulo

