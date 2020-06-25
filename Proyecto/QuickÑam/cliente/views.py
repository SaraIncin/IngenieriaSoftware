"""Views cliente."""
from decimal import Decimal
# Django
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

#Forms
from admin_repartidor.forms import RegistrarRepartidorForm, EditarRepartidorForm
from usuarios.forms import UbicacionForm

#Models
from .models import Carrito, ArticuloCarrito, Orden
from admin_repartidor.models import Repartidor
from admin_alimentos.models import Alimento
from admin_categoria.models import Categoria
from usuarios.models import Cliente, Ubicacion

#Utils
from .utils import OrderIdGenerator


# Class-based views.
class ClienteMenu(View):
    """ADMIN index Repartidor. """

    template = "cliente_menu.html"

    def get(self, request):
        alimentos = Alimento.objects.all()
        context = {"alimentos": alimentos, "categorias": Categoria.objects.all()}
        return render(request, self.template, context)

    		
class ListaPedidos(View):
    template = "carrito/carrito_list.html"

    def get(self, request):
        cliente = Cliente.objects.get(user=request.user)
        pedidos = Orden.objects.filter(user = cliente)
        context = {"pedidos":pedidos}
        return render(request, self.template, context)

class CarritoDetalle(LoginRequiredMixin, View):
    template = "carrito/carrito.html"
    def get(self, request):
        carrito= Carrito.objects.filter(user = request.user.id).filter(completado = False).first()
        if carrito == None:
            carrito = Carrito(user=request.user)
            carrito.save()
        articulos = ArticuloCarrito.objects.filter(carrito = carrito.id)
        context = {"pedidos": carrito, "articulos":articulos}
        return render(request, self.template, context)


class AgregarArticulo(View):

    def post(self, request, id):
        alimento = Alimento.objects.get(id = id)
        carrito= Carrito.objects.filter(user = request.user.id).filter(completado = False).first()
        if carrito == None:
            carrito = Carrito(user= request.user.id)
            carrito.save()

        item = ArticuloCarrito.objects.filter(carrito = carrito.id).filter(producto = alimento).first()
        if item == None:
            item = ArticuloCarrito.objects.create(producto = alimento, precio = alimento.precio, carrito = carrito)
        elif item.producto == alimento:
            var = item.cantidad + 1
            ArticuloCarrito.objects.filter(carrito = carrito.id).filter(id = item.id).update(cantidad= var)

        return HttpResponse(item, status=200)


class ModificarCantidadArticulo(View):

    def post(self, request, id):
        alimento = Alimento.objects.get(id = id)
        carrito= Carrito.objects.filter(user = request.user.id).filter(completado = False).first()
        item = ArticuloCarrito.objects.filter(carrito = carrito.id).filter(producto = alimento).first()
        if item.cantidad == 1:
            return
        var = item.cantidad - 1
        ArticuloCarrito.objects.filter(carrito = carrito.id).filter(id = item.id).update(cantidad= var)

        return HttpResponse(item, status=200)


class EliminarArticulo(View):

    def post(self, request, id):
        alimento = Alimento.objects.get(id = id)
        carrito= Carrito.objects.filter(user = request.user.id).filter(completado = False).first()
        item = ArticuloCarrito.objects.filter(carrito = carrito.id).filter(producto = alimento).first()
        
        ArticuloCarrito.objects.filter(carrito= carrito.id).filter(id = item.id).delete()

        return HttpResponse(item, status=200)


class agregarUbicacion(View):
    template = "carrito/agregar_ubicacion.html"

    def get(self,request,id):
        form = UbicacionForm()
        carrito = Carrito.objects.get(id=id)
        context = {"form": form, "carrito":carrito}
        return render(request, self.template, context)

    def post(self,request, id):
        form = UbicacionForm(request.POST)
        carrito = Carrito.objects.get(id=id)
        if not form.is_valid():
            context = {"form": form, "carrito":carrito}
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
        return redirect('cliente:confirmar_direccion', id=id)
        
class ListaUbicaciones(View):
    template = "carrito/ver_direcciones.html"
    def get(self,request,id):
        if request.user.is_authenticated and not request.user.is_anonymous:
            cliente = Cliente.objects.get(user = request.user.id)
            direcciones = Ubicacion.objects.filter(cliente = cliente.id)
            carrito = Carrito.objects.get(id=id)
            context = {"direcciones":direcciones,"carrito":carrito}
            return render(request, self.template, context)
        
class DetalleOrden(View):
    template = "carrito/ver_orden.html"
    def get(self,request,id, id_ubicacion):
        order_id = OrderIdGenerator.generate_order_id()
        if request.user.is_authenticated and not request.user.is_anonymous:
            cliente = Cliente.objects.get(user=request.user)
            carrito = Carrito.objects.get(id=id)
            carrito.completado=True
            carrito.save()
            articulos=ArticuloCarrito.objects.filter(carrito=carrito)
            total=Decimal(0.0)
            for articulo in articulos:
                total+=(articulo.producto.precio*articulo.cantidad)
            ubicacion=Ubicacion.objects.get(id=id_ubicacion)
            order = Orden(carrito=carrito, order_id=order_id, user=cliente, ubicacion=ubicacion, total=total)
            order.save()
        ordenes= Orden.objects.filter(order_id=order_id)
        context = {'ordenes': ordenes}
        return render(request, self.template, context)

class CarritoPedido(LoginRequiredMixin, View):
    template = "carrito/carrito_pedido.html"
    def get(self, request, id):
        carrito= Carrito.objects.get(id=id)
        orden= Orden.objects.get(carrito=carrito.id)
        articulos = ArticuloCarrito.objects.filter(carrito = carrito.id)
        context = {"carrito": carrito, "articulos":articulos, "orden":orden}
        return render(request, self.template, context)




