from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SurForm(forms.Form):
    lugar = forms.CharField(max_length=150)
    descripcion = forms.CharField(max_length=3000)
    precio = forms.IntegerField()

class NorteForm(forms.Form):
    lugar = forms.CharField(max_length=150)
    descripcion = forms.CharField(max_length=3000)
    precio = forms.IntegerField()

class CentroForm(forms.Form):
    lugar = forms.CharField(max_length=150)
    descripcion = forms.CharField(max_length=3000)
    precio = forms.IntegerField()

class RegistrarUser(UserCreationForm):
    username = forms.CharField(label="Ingrese su nombre de usuario")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditarUser(UserCreationForm):
    username = forms.CharField(label="Editar su nombre de usuario")
    password1 = forms.CharField(label="Cambiar su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar su contraseña nueva", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
