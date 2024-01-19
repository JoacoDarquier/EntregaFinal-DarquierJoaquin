from django.db import models

class Arquero (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()

class Defensor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()

class Mediocampista (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()

class Delantero (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pie_habil = models.CharField(max_length=20)
    cant_clubes_anteriores = models.IntegerField()
    telefono = models.IntegerField()
    estatura = models.FloatField()
    email = models.EmailField()

