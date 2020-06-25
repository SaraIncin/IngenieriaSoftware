"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from . import views

urlpatterns = [
	path("", views.Inicio.as_view(), name="inicio"),
    path('login-cliente/', views.LoginViewCliente.as_view(), name='login_cliente'),
    path('login-repartidor/', views.LoginViewRepartidor.as_view(), name='login_repartidor'),
    path('login-administrador/', views.LoginViewAdministrador.as_view(), name='login_administrador'),
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
    path("direccion/", views.UbicacionView.as_view(), name="direccion"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("cliente/", views.InicioCliente.as_view(), name="inicio_cliente"),
    path("repartidor/", views.InicioRepartidor.as_view(), name="inicio_repartidor"),
    path("repartidor/proceso-entrega/", views.ProcesoEntrega.as_view(), name="proceso_entrega"),
    path("repartidor/entregada/", views.Recibida.as_view(), name="entregada"),
    path("repartidor/seleccionar/<int:id>", views.SeleccionarOrden.as_view(), name = "seleccionar_orden"),
    path("repartidor/cambiar-estado/<int:id>", views.Entregado.as_view(), name = "modificar_estado"),
    path("repartidor/ver-pedido/<int:id>", views.DetalleOrden.as_view(),name="ver_pedido"),
]