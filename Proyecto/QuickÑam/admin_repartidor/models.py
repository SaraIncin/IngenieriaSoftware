from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Repartidor(models.Model):
    """Extended user."""

    repartidor = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.IntegerField(default=1)

    
