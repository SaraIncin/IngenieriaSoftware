"""ADMIN URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path


# Views
from cliente import views

app_name = "cliente"
urlpatterns = [
    path('menu/', views.ClienteMenu.as_view(), name='menucliente'),
    path('ver-carrito/', views.CarritoDetalle.as_view(), name ='ver_carrito'),
    path('carrito-pedido/<int:id>', views.CarritoPedido.as_view(), name ='carrito_pedido'),
    path('ver-pedidos/', views.ListaPedidos.as_view(), name = 'ver_pedidos'),    
    path('menu/<int:id>', views.AgregarArticulo.as_view(), name="agregar_producto"),
    path('carrito/<int:id>', views.ModificarCantidadArticulo.as_view(), name="modificar_producto"),
    path('carrito/articulo/<int:id>', views.EliminarArticulo.as_view(), name="eliminar_producto"),
    path('completar-orden/<int:id>/<int:id_ubicacion>', views.DetalleOrden.as_view(), name ='completar_orden'),
    path('confirmar-direccion/<int:id>', views.ListaUbicaciones.as_view(), name ='confirmar_direccion'),
    path('agregar-direccion/<int:id>', views.agregarUbicacion.as_view(), name ='agregar_direccion')
]
