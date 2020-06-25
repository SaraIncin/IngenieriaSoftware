"""ADMIN URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path


# Views
from admin_alimentos import views

app_name = "admin_alimentos"
urlpatterns = [
    path('registrar-alimento/', views.RegistrarAlimento.as_view(), name='registrar_alimento'),
    path('ver-alimento/', views.VerAlimento.as_view(), name='ver_alimento'),
    path('ver-alimento/<int:id>', views.EditarAlimento.as_view(), name='editar_alimento'),
    path('eliminar-alimento/<int:id>', views.EliminarAlimento.as_view(), name='eliminar_alimento'),
    path('ver-alimento/eliminar/<int:id>', views.Modal.as_view(), name = 'modal'),
]