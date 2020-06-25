from django.db import models
from django.urls import reverse

from admin_categoria.models import Categoria

# Create your models here.

class Alimento(models.Model):
	"""Alimentos"""
	nombre = models.CharField(max_length=200)
	precio = models.IntegerField()
	foto = models.ImageField(blank=True, upload_to = 'fotos')
	descripcion =models.CharField(max_length=300)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 

	def get_absolute_url(self):
		return reverse('admin_alimentos:ver_alimento')
