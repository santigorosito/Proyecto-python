from django.db import models
from django.contrib.auth.models import User

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

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Se puede editar cualquier models(como norte, sur, centro)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
    def __str__(self):
        return f"{self.usuario} --- {self.image}"


