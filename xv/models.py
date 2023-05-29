from django.db import models

class Invitado(models.Model):
    nombre = models.CharField(max_length=50)
    relacion = models.CharField(max_length=20)
    asistentes = models.CharField(max_length=20)
    dedicatoria = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre