from django.db import models

class Sur(models.Model):
    lugar = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()

class Norte(models.Model):
    lugar = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()

class Centro(models.Model):
    lugar = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    precio = models.IntegerField()


