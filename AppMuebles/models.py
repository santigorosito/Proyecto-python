from django.db import models

class Serie(models.Model):

    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)

