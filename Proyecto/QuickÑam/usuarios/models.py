from django.db import models

from django.contrib.auth.models import User



class Cliente(models.Model):
    """Extended user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=14)
    tipo=models.IntegerField(default=2)


class Administrador(models.Model):
    administrador = models.OneToOneField(User, on_delete=models.CASCADE, default = "")
    tipo=models.IntegerField(default=0)


class Ubicacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    delegacion = models.CharField(max_length=50)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    cp = models.CharField(max_length= 5)



