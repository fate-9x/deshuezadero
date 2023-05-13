from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput
from appDeshuezadero.models import *

generos = []
comunas = []

for genero in Genero.objects.all():
    generos.append((genero.id, genero.nombre))

for comuna in Comuna.objects.all():
    comunas.append((comuna.id, comuna.nombre))


class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo', 'autocomplete': 'off'}))

    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}))


class Formulario_Registro(forms.Form):

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
        attrs={'class': 'form-select'}), choices=generos)

    comuna = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select'}), choices=comunas)
