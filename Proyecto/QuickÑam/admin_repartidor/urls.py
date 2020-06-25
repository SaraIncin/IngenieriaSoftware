"""ADMIN URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path


# Views
from admin_repartidor import views

app_name = "admin_repartidor"
urlpatterns = [
    path('', views.Index.as_view(), name='principal'),
    path('registrar-repartidor/', views.RegistrarRepartidor.as_view(), name='registrar_repartidor'),
    path('ver-repartidor/', views.VerRepartidor.as_view(), name='ver_repartidor'),
    path('ver-repartidor/<int:id>', views.EditarRepartidor.as_view(), name='editar_repartidor'),
    path('eliminar-repartidor/<int:id>', views.EliminarRepartidor.as_view(), name='eliminar_repartidor'),
    path('ver-orden/<int:id>', views.VerOrden.as_view(), name='ver_orden'),
    path('ver-pedidos/cambiar-estado/<int:id>', views.ModificarEstado.as_view(), name='cambiar_estado'),
    path('ver-pedidos/estado/<int:estado>', views.VerEstado.as_view(), name = 'ver_estado'),
]