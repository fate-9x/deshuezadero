from django.shortcuts import render
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from appDeshuezadero.models import *
from datetime import datetime, date, timedelta
from utilidades import utilidades
import time
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .forms import *

# Create your views here.


def formulario_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = Formulario_Login(request.POST or None)
    mensaje = ''
    if request.method == 'POST':
        if form.is_valid:
            user = authenticate(
                request, username=request.POST['correo'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                usersMetadata = Cliente.objects.filter(
                    user_id=request.user.id).get()
                request.session['users_metadata_id'] = usersMetadata.id
                return HttpResponseRedirect('/')
            else:
                mensaje = f"El correo o la contraseña son incorrectos."
                messages.add_message(request, messages.ERROR, mensaje)
    return render(request, 'account/login.html', {'form': form,  'mensaje': mensaje})


def formulario_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':

        form = Formulario_Registro(request.POST or None)

        if form.is_valid:
            existCorreo = User.objects.filter(
                username=request.POST['correo']).count()

            existRut = Cliente.objects.filter(
                rut=request.POST['rut']).count()

            if existCorreo != 0:
                mensaje = f"El correo ingresado ya existe, por favor ingrese un nuevo correo."
                messages.add_message(request, messages.WARNING, mensaje)

            elif existRut != 0:
                mensaje = f"El rut ingresado ya existe, por favor ingrese un nuevo rut."
                messages.add_message(request, messages.WARNING, mensaje)

            elif request.POST['password'] != request.POST['password2']:
                mensaje = f"Las contraseñas ingresadas no coinciden, por favor ingrese nuevamente las contraseñas."
                messages.add_message(request, messages.WARNING, mensaje)

            else:

                comuna = Comuna.objects.filter(
                    nombre=request.POST['comuna'].lower()).get()
                region = Region.objects.filter(
                    nombre=request.POST['region'].lower()).get()

                if comuna.region_id == region.id:

                    u = User.objects.create_user(username=request.POST['correo'],
                                                 password=request.POST['password'],
                                                 email=request.POST['correo'],
                                                 first_name=request.POST['nombre'],
                                                 last_name=request.POST['apellido'],
                                                 is_active=1)
                    Cliente.objects.create(correo=request.POST['correo'],
                                           rut=request.POST['rut'],
                                           user_id=u.id,
                                           genero_id=request.POST['genero'],
                                           comuna_id=comuna.id,
                                           tipo_cliente_id=request.POST['tipo_cliente'])

                    mensaje = f"El usuario {request.POST['correo']} ha sido creado con éxito, por favor inicie sesión."
                    messages.add_message(request, messages.SUCCESS, mensaje)

    form = Formulario_Registro()
    return render(request, 'account/register.html', {'form': form})


def logout_account(request):

    if request.user.is_authenticated:

        logout(request)
        return HttpResponseRedirect('/')
    return None
