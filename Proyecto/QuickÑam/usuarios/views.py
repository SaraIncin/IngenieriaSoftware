from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#models
from .models import Administrador, Cliente, Ubicacion
from admin_repartidor.models import Repartidor
from admin_categoria.models import Categoria 
from cliente.models import Orden, Carrito, ArticuloCarrito, RepartidorOrden


# Create your views here.
from .forms import ExtendedUserCreationForm, UserClientForm,LoginFormCliente,LoginFormAdmin,LoginFormRepartidor, UbicacionForm
            
class SignUpView(View):
    """New User Sign Up."""

    template = "Usuarios/registro.html"

    def get(self, request):
        """Render sign up form."""
        form = ExtendedUserCreationForm()
        cliente_form = UserClientForm()
        ubicacion_form = UbicacionForm()
        context = {"form": form, "cliente_form": cliente_form, "ubicacion_form": ubicacion_form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = ExtendedUserCreationForm(request.POST)
        cliente_form = UserClientForm(request.POST)
        ubicacion_form = UbicacionForm(request.POST)
        if not form.is_valid() or not cliente_form.is_valid():
            context = {"form": form, "cliente_form": cliente_form, "ubicacion_form": ubicacion_form}
            return render(request, self.template, context)

        user = form.save()
        cliente = cliente_form.save(commit=False)
        cliente.user=user
        cliente.save()
        ubicacion = ubicacion_form.save(commit = False)
        ubicacion.cliente = cliente
        ubicacion.save()   

        return redirect("usuarios:login_cliente")

class UbicacionView(View):
    template = "Usuarios/ubicacion.html"

    def get(self, request):
        """Render register form."""
        form = UbicacionForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate register form."""
        form = UbicacionForm(request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)
        if request.user.is_authenticated and not request.user.is_anonymous:
            cliente=Cliente.objects.get(user=request.user)
            Ubicacion.objects.create(
                cliente=cliente,   
                delegacion=form.cleaned_data["delegacion"],
                calle=form.cleaned_data["calle"],
                numero=form.cleaned_data["numero"],
                cp=form.cleaned_data["cp"]
            )
        return redirect("usuarios:inicio_cliente")

class LoginViewCliente(View):
    """User Login."""

    template = "Usuarios/login.html"

    def get(self, request):
        """Render sign up form."""
        form = LoginFormCliente()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginFormCliente(data=request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        ) 

        login(request, user)    
        if not Cliente.objects.filter(user = user.id).first() == None:
            return redirect("usuarios:inicio_cliente")
        else:
            return redirect("usuarios:login_cliente")


class LoginViewAdministrador(View):
    """User Login."""

    template = "Usuarios/login_admin.html"

    def get(self, request):
        """Render sign up form."""
        form = LoginFormAdmin()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginFormAdmin(data=request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        login(request, user)                

        if not Administrador.objects.filter(administrador = user.id).first() == None:  
            return redirect("admin_repartidor:principal")
        else:
            return redirect("usuarios:login_administrador")


class LoginViewRepartidor(View):
    """User Login."""

    template = "Usuarios/login_repartidor.html"

    def get(self, request):
        """Render sign up form."""
        form = LoginFormRepartidor()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginFormRepartidor(data=request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )

        login(request, user)            

        if not Repartidor.objects.filter(repartidor = user.id).first() == None:
            return redirect("usuarios:inicio_repartidor")
        else:
            return redirect("usuarios:login_repartidor")
            

class LogoutView(View):
    """Logout View."""

    def get(self, request):
        """Logout logged user."""
        # As simple as.
        logout(request)
        return redirect("usuarios:inicio")

class Inicio(View):
    """New User Sign Up."""

    template = "principal.html"

    def get(self, request):
        """Render sign up form."""
        return render(request, self.template) 

class InicioCliente(View):
    """New User Sign Up."""

    template = "cliente.html"

    def get(self, request):
        categoria = Categoria.objects.all()
        context = {"categorias":categoria, "var" : Categoria.objects.first()}
        return render(request, self.template, context) 

class InicioRepartidor(View):
    """New User Sign Up."""

    template = "repartidor.html"

    def get(self, request):
        """Render sign up form."""
        ordenes = Orden.objects.filter(estado = 1)
        productos = ArticuloCarrito.objects.all()
        contexto = {"pedidos": ordenes, "productos" : productos}
        return render(request, self.template,contexto)  

class ProcesoEntrega(View):
    """."""

    template = "repartidor_entregas.html"

    def get(self, request):
        """Render sign up form."""
        ordenes = Orden.objects.filter(estado = 2)
        productos = ArticuloCarrito.objects.all()
        contexto = {"pedidos": ordenes, "productos" : productos}
        return render(request, self.template,contexto)

class Recibida(View):
    """New User Sign Up."""

    template = "repartidor_orden_entregada.html"

    def get(self, request):
        """Render sign up form."""
        ordenes = Orden.objects.filter(estado = 3)
        productos = ArticuloCarrito.objects.all()
        contexto = {"pedidos": ordenes, "productos" : productos}
        return render(request, self.template,contexto)                                       
        

class SeleccionarOrden(View):

    def post(self, request, id):
        orden = Orden.objects.get(id = id)
        repartidor = Repartidor.objects.get(repartidor = request.user.id)
        RepartidorOrden.objects.create(orden = orden, repartidor = repartidor)
        Orden.objects.filter(id = id).update(estado= 2)

        return HttpResponse(orden, status = 200)


class Entregado(View):

    def post(self, request, id):
        orden = Orden.objects.get(id = id)
        Orden.objects.filter(id = id).update(estado= 3)

        return HttpResponse(orden, status = 200)

class DetalleOrden(View):

    template = "ver_orden.html"

    def get(self,request, id):
        orden = Orden.objects.get(id = id)
        productos = ArticuloCarrito.objects.filter(carrito = orden.carrito)
        print(productos)
        contexto = {"orden":orden, "productos":productos}
        return render(request, self.template, contexto)
