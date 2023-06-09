from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput
from appDeshuezadero.models import *
from utilidades import utilidades as ut


class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo', 'autocomplete': 'off'}))

    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}))


class Formulario_Registro(forms.Form):

    generos, tipos_clientes = ut.formularioRegistroChoices()

    rut = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rut', 'autocomplete': 'off'}))

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete': 'off'}))

    apellido = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete': 'off'}))

    correo = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo', 'autocomplete': 'off'}))

    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}))

    password2 = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}))

    genero = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select input-select'}), choices=generos)

    region = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Region', 'autocomplete': 'off'}))

    comuna = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Comuna', 'autocomplete': 'off'}))

    foto = forms.ImageField(widget=forms.FileInput())

    tipo_cliente = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select input-select'}), choices=tipos_clientes)

# Si al borrar la base de datos y volver a crearla da error 1146, comentar todo el formulario
