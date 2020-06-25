from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse 
from django.views.generic.edit import DeleteView, UpdateView
from .forms import CategoriaForm 
from .models import Categoria
from django.urls import reverse

class RegistrarCategoriaView(View):
    """New Categoria."""

    template = "admin_categoria/registrar_categoria.html"

    def get(self, request):
        """Render sign up form."""
        form = CategoriaForm()
        contexto = {"form": form}
        return render(request, self.template, contexto)

    def post(self, request):
        """Receive and validate sign up form."""
        form = CategoriaForm(request.POST, request.FILES)
        contexto = {"form": form}
        if not form.is_valid():
            return render(request, self.template, contexto)
        categoria = Categoria.objects.create(
        	nombre=form.cleaned_data["nombre"],
            foto=form.cleaned_data["foto"],
            descripcion=form.cleaned_data["descripcion"],
        )
        return redirect('admin_categoria:ver_categoria')

class VerCategoriaView(View):
	"""Ver categoria"""
	template = "admin_categoria/categoria_list.html"

	def get(self, request):
		categoria = Categoria.objects.all()
		context = {"categorias": categoria}
		return render(request, self.template, context)  
    
class EditarCategoriaView(UpdateView):
    form_class = CategoriaForm

    def get_object(self):
    	id_ = self.kwargs.get("id")
    	return get_object_or_404(Categoria, id = id_)

    def form_valid(self,form):
    	print(form.cleaned_data)
    	return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin_categoria:ver_categoria')
    	
class EliminarCategoriaView(DeleteView):

    def get_object(self):
    	id_ = self.kwargs.get("id")
    	return get_object_or_404(Categoria, id = id_)

    def get_success_url(self):
    	return reverse('admin_categoria:ver_categoria')

