from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput
from appDeshuezadero.models import *
from utilidades import utilidades as ut

tipos_repuestos = []

for tipos in TipoRepuesto.objects.all():
    tipos_repuestos.append((tipos.id, tipos.tipo))


class Formulario_Repuestos(forms.Form):

    foto = forms.ImageField(widget=forms.FileInput())

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete': 'off'}))

    precio = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}))

    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}))

    tipo_repuesto = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select'}), choices=tipos_repuestos)
