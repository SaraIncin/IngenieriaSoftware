from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from admin_alimentos.models import Alimento
from usuarios.models import Cliente, Ubicacion
from admin_repartidor.models import Repartidor

class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)
    completado = models.BooleanField(default = False)

class ArticuloCarrito(models.Model):
    producto = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio = models.FloatField(blank=True)
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    
ORDER_STATUS = (
    (0, 'Recibido'),
    (1, 'Listo para entregar'),
    (2, 'En proceso de entrega'),
    (3, 'Entregado'),
)

class Orden(models.Model):
    user = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.CharField(unique=True, max_length=120, default='abc')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True)
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    estado = models.IntegerField(default = 0, choices=ORDER_STATUS, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=1000.0, max_digits=300, decimal_places=2)

class RepartidorOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
