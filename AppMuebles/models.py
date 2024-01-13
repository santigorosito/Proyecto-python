from django.db import models

class Sur(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()

class Norte(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()

class Centro(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()


