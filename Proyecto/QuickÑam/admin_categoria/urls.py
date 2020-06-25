"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from . import views
app_name = "admin_categoria"
urlpatterns = [
    path("registro-categoria/", views.RegistrarCategoriaView.as_view(), name="registro_categoria"),
    path("ver-categoria/", views.VerCategoriaView.as_view(), name="ver_categoria"),
    path('editar-categoria/<int:id>', views.EditarCategoriaView.as_view(), name="editar_categoria"),
    path("eliminar-categoria/<int:id>", views.EliminarCategoriaView.as_view(), name="eliminar_categoria"),    
]
