from django.contrib import admin

from .models import Carrito, ArticuloCarrito, Orden, RepartidorOrden

admin.site.register(Carrito)
admin.site.register(ArticuloCarrito)
admin.site.register(Orden)
admin.site.register(RepartidorOrden)