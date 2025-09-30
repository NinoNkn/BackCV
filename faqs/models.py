from django.db import models

class FAQ(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta

