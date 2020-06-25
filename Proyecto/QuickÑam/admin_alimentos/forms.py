"""Users forms."""
# Django
from django import forms

#Models
from admin_alimentos.models import Alimento


class RegistrarAlimentoForm(forms.ModelForm):
    """."""
    class Meta:
        model = Alimento
        fields = ( "nombre","precio","foto", "descripcion","categoria")
      