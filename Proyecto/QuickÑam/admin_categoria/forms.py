"""Users forms."""
# Django
from django import forms

#Models
from .models import Categoria


class CategoriaForm(forms.ModelForm):
    """."""
    class Meta:
        model = Categoria
        fields = ("nombre","foto", "descripcion")

