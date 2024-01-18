from django import forms

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