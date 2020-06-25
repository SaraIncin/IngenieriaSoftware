from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.utils.module_loading import import_string
from django.utils.translation import gettext as _, ngettext
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import Cliente, Administrador, Ubicacion
from admin_repartidor.models import Repartidor
from django.core.validators import RegexValidator

class ExtendedUserCreationForm(UserCreationForm):
    letter = RegexValidator(r'^([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)?\s?([A-ZÑÁÉÍÓÚ][a-zñáéíóú]*)$', 'Solo letras')
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=255, validators=[letter])
    apellido = forms.CharField(max_length=255, validators=[letter])

    class Meta:
        model = User
        fields = ('email', 'nombre', 'apellido', 'password1', 'password2')

    password1 = forms.CharField(
    label="Contraseña",
    strip=False,
    widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
    label= "Confirmación de contraseña",
    widget=forms.PasswordInput,
    strip=False,
    help_text= "Ingrese la misma contraseña que antes para la verificación.",
    )

    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }


    def clean_email(self):
        """Validar que el email ya exista en la base
        Just validating email field.
        """
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("Este email ya existe.")

        return data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellido']

        if commit:
            user.save()
        return user
        
class UserClientForm(forms.ModelForm):
    """Form for sign up"""
    numb=RegexValidator(r'^[0-9]*$', 'Telefono incorrecto')
    telefono = forms.CharField(max_length=14, validators=[numb])
    class Meta:
        model = Cliente
        fields = ('telefono',)

class UbicacionForm(forms.ModelForm):
    delegacion = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=255)
    numero = forms.CharField(max_length=5)
    cp = forms.CharField(max_length=5)
    class Meta:
        model = Ubicacion
        fields = ('delegacion', 'calle', 'numero', 'cp')
        
class LoginFormCliente(AuthenticationForm):
    """Login form."""
    username = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label = "Contraseña")

    def clean(self):
        """Validate data.
        Validating all fields.
        """
        username = self.data["username"]
        password = self.data["password"]

        if User.objects.filter(username=username).count() == 0:
            self.add_error(
                "username", forms.ValidationError("El correo ingresado no existe")
            )

        # authenticate search for the user with that username and password.
        # authenticate do not log any user.
        user = authenticate(username=username, password=password)
        
        if user is None:
            self.add_error("password", forms.ValidationError("Contraseña erronea"))
        else:
            cliente =  Cliente.objects.filter(user = user.id).first()
            if cliente is None:
                self.add_error(
                    "username", forms.ValidationError("Este usuario no es cliente")
                    )

class LoginFormAdmin(AuthenticationForm):
    """Login form."""
    username = forms.EmailField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label = "Contraseña")

    def clean(self):
        """Validate data.
        Validating all fields.
        """
        username = self.data["username"]
        password = self.data["password"]

        if User.objects.filter(username=username).count() == 0:
            self.add_error(
                "username", forms.ValidationError("El email ingresado no existe")
            )

        # authenticate search for the user with that username and password.
        # authenticate do not log any user.
        user = authenticate(username=username, password=password)
        
        if user is None:
            self.add_error("password", forms.ValidationError("Contraseña errónea"))
        else:
            admin = Administrador.objects.filter(administrador = user.id).first()
            if admin is None:
                self.add_error(
                    "username", forms.ValidationError("Este usuario no es administrador")
                    )

class LoginFormRepartidor(AuthenticationForm):
    """Login form."""
    username = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label = "Contraseña")

    def clean(self):
        """Validate data.
        Validating all fields.
        """
        username = self.data["username"]
        password = self.data["password"]

        if User.objects.filter(username=username).count() == 0:
            self.add_error(
                "username", forms.ValidationError("El email ingresado no existe.")
            )

        # authenticate search for the user with that username and password.
        # authenticate do not log any user.
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error("password", forms.ValidationError("Contraseña errónea"))
        else:
            repartidor = Repartidor.objects.filter(repartidor = user.id).first()
            if repartidor is None:
                self.add_error(
                    "username", forms.ValidationError("Este usuario no es repartidor.")
                    )
