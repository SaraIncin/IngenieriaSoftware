"""Users forms."""
# Django
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

#Models
from .models import Repartidor


class RegistrarRepartidorForm(forms.Form):
    """."""
    letter = RegexValidator(r'^([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)?\s?([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)$', 'Solo letras')
    nombre = forms.CharField(max_length=255, validators=[letter])
    apellido = forms.CharField(max_length=255, validators=[letter])
    email = forms.EmailField(max_length=255)

    def clean_email(self):
        """Validate that the email doesn't exist in the database."""
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("This email already exists.")
        return data


class EditarRepartidorForm(forms.ModelForm):
    """."""
    class Meta:
        model = User
        fields = ( "first_name","last_name","email")

        labels = {"first_name" : 'Nombre', "last_name": 'Apellido', 'email' : 'Email'}
        widgets = {"first_name" : forms.TextInput(), "last_name": forms.TextInput(), 
        'email' : forms.TextInput()}

    letter = RegexValidator(r'^([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)?\s?([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)$', 'Solo letras')
    first_name = forms.CharField(
    validators=[letter],
    strip=False,
    )
    last_name = forms.CharField(
    validators=[letter],
    strip=False,
    )

        

      