"""ADMIN Views Alimentos."""
# Django
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse

#Forms
from admin_alimentos.forms import RegistrarAlimentoForm

#Models
from admin_alimentos.models import Alimento
from admin_categoria.models import Categoria


class RegistrarAlimento(View):
    """New Alimento."""

    template = "admin_alimentos/registrar.html"

    def get(self, request):
        """Render sign up form."""
        form = RegistrarAlimentoForm()
        contexto = {"form": form}
        return render(request, self.template, contexto)

    def post(self, request):
        """Receive and validate sign up form."""
        form = RegistrarAlimentoForm(request.POST, request.FILES)
        contexto = {"form": form}
        if not form.is_valid():
            return render(request, self.template, contexto)
        alimento = Alimento.objects.create(
        	nombre=form.cleaned_data["nombre"],
        	precio=form.cleaned_data["precio"],
            foto=form.cleaned_data["foto"],
            descripcion=form.cleaned_data["descripcion"],
            categoria = form.cleaned_data["categoria"]
        )
        return redirect('admin_alimentos:ver_alimento')


class VerAlimento(View):
	"""Ver lista de alimentoes"""
	template = "admin_alimentos/alimentos_list.html"

	def get(self, request):
		alimentos = Alimento.objects.all()
		context = {"alimentos": alimentos, "categorias": Categoria.objects.all()}
		return render(request, self.template, context)    

class EditarAlimento(UpdateView):
    form_class = RegistrarAlimentoForm

    def get_object(self):
    	id_ = self.kwargs.get("id")
    	return get_object_or_404(Alimento, id = id_)

    def form_valid(self,form):
    	print(form.cleaned_data)
    	return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin_alimentos:ver_alimento')

class EliminarAlimento(DeleteView):

    def get_object(self):
    	id_ = self.kwargs.get("id")
    	return get_object_or_404(Alimento, id = id_)

    def get_success_url(self):
    	return reverse('admin_alimentos:ver_alimento')

class Modal(View):
    template = "admin_alimentos/modal.html"

    def get(self, request, id):
        alimentos = Alimento.objects.get(id = id)
        context = {"alimento": alimentos}
        return render(request, self.template, context)
