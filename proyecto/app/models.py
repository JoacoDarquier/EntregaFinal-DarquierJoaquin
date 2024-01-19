from django.db import models
from django.utils import timezone
from datetime import timedelta

def calcular_fecha_nacimiento_predeterminada():
    return timezone.now() - timedelta(days=365*25)

class Arquero (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()
    fecha_nacimiento = models.DateTimeField(default=calcular_fecha_nacimiento_predeterminada)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.pie_habil}, {self.cant_clubes_anteriores}, {self.telefono}, {self.estatura}, {self.email}, {self.fecha_nacimiento}"


class Defensor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()
    fecha_nacimiento = models.DateTimeField(default=calcular_fecha_nacimiento_predeterminada)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.pie_habil}, {self.cant_clubes_anteriores}, {self.telefono}, {self.estatura}, {self.email}, {self.fecha_nacimiento}"


class Mediocampista (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()
    fecha_nacimiento = models.DateTimeField(default=calcular_fecha_nacimiento_predeterminada)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.pie_habil}, {self.cant_clubes_anteriores}, {self.telefono}, {self.estatura}, {self.email}, {self.fecha_nacimiento}"


class Delantero (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()
    fecha_nacimiento = models.DateTimeField(default=calcular_fecha_nacimiento_predeterminada)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.pie_habil}, {self.cant_clubes_anteriores}, {self.telefono}, {self.estatura}, {self.email}, {self.fecha_nacimiento}"