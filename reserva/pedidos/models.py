from django.db import models
from datetime import datetime ,time

# Create your models here.


class Aula (models.Model):
    nombre = models.CharField(max_length=60)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.nombre)


class Recurso (models.Model):
    nombre = models.CharField(max_length=60)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.nombre)


class Profesor (models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=60)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return "{} {}".format(self.apellido, self.nombre)


class Reserva (models.Model):
    fecha = models.DateField(default=datetime.now)
    desde = models.TimeField()
    hasta = models.TimeField()
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.fecha, self.desde, self.hasta,
                                          self.aula, self.recurso, self.profesor)
