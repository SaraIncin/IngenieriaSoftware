from django.db import models
from django.urls import reverse

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	foto = models.ImageField(blank=True, upload_to = 'fotos')
	descripcion = models.CharField(max_length=300)

	def __str__(self):
		"""Get str representation."""
		return self.nombre
		
	def __repr__(self):
		"""Get str representation."""
		return self.__str__()

	def get_absolute_url(self):
		return reverse('admin_categoria:ver_categoria')	
	
