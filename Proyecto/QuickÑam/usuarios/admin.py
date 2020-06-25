from django.contrib import admin
from .models import  Administrador, Cliente, Ubicacion

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Ubicacion)


