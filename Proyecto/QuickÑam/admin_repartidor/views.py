"""ADMIN Views repartidor."""
# Django
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

#Forms
from admin_repartidor.forms import RegistrarRepartidorForm, EditarRepartidorForm

#Models
from admin_repartidor.models import Repartidor
from cliente.models import Orden, ArticuloCarrito, Carrito



# Class-based views.
class Index(View):
    """ADMIN index Repartidor. """

    template = "admin_repartidor/index.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)


class RegistrarRepartidor(View):
    """New Repartidor."""

    template = "admin_repartidor/registrar.html"

    def get(self, request):
        """Render sign up form."""
        form = RegistrarRepartidorForm()
        contexto = {"form": form}
        return render(request, self.template, contexto)

    def post(self, request):
        """Receive and validate sign up form."""
        form = RegistrarRepartidorForm(request.POST)
        contexto = {"form": form}
        print(form)
        if not form.is_valid():
            return render(request, self.template, contexto)
        contraseña = BaseUserManager.make_random_password(self,length = 20)
        email=form.cleaned_data["email"]        
        user = User.objects.create_user(
        	username=email,
        	email=email,
            password = contraseña,
            first_name=form.cleaned_data["nombre"],
            last_name=form.cleaned_data["apellido"],
        )
        if user:
            Repartidor.objects.create(repartidor=user)
            body = render_to_string('admin_repartidor/mensaje.html', {'contraseña':contraseña})
            mensaje = EmailMessage(subject = 'Confirmación de cuenta',
                body = body, to = [email])
            mensaje.content_subtype = "html" 
            mensaje.send()
            return redirect("admin_repartidor:ver_repartidor")
        else:
            return redirect("admin_repartidor:ver_repartidor")


class VerRepartidor(View):
	"""Ver lista de repartidores"""
	template = "admin_repartidor/repartidor_list.html"

	def get(self, request):
		repartidores = User.objects.all()
		context = {"repartidores":repartidores}
		return render(request, self.template, context)



class EditarRepartidor(UpdateView):

    form_class = EditarRepartidorForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id = id_)

    def form_valid(self,form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin_repartidor:ver_repartidor')


class EliminarRepartidor(DeleteView):
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id = id_)

    def get_success_url(self):
        return reverse('admin_repartidor:ver_repartidor')



class VerOrden(View):
    template = "admin_repartidor/order_list_admin.html"

    def get(self, request, id):
        """GET Method"""
        orden = Orden.objects.get(id = id)
        articulos = ArticuloCarrito.objects.filter(carrito = orden.carrito)
        contexto = {"orden" : orden, "alimentos" : articulos}
        return render(request,self.template, contexto)

class VerEstado(View):

    template = "admin_repartidor/admin_orden.html"

    def get(self, request,estado):
        if estado == 0:
            orden = Orden.objects.filter(estado=0)
        elif estado == 1:
            orden = Orden.objects.filter(estado=1)
        elif estado == 2:
            orden = Orden.objects.filter(estado=2)
        elif estado == 3:
            orden = Orden.objects.filter(estado=3)
        articulos = ArticuloCarrito.objects.all()
        contexto = {"pedidos" : orden, "alimentos" : articulos, "estado": estado}
        return render(request,self.template, contexto)


class ModificarEstado(View):

    def post(self, request, id):
        orden = Orden.objects.get(id = id)
        Orden.objects.filter(id = id).update(estado= 1)

        return HttpResponse(orden, status=200)