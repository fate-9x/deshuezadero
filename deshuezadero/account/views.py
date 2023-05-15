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
                messages.add_message(
                    request, messages.WARNING, f'Los datos ingresados no son correctos, Por favor intentelo nuevamente.')
    return render(request, 'account/login.html', {'form': form})


def formulario_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    form = Formulario_Registro(request.POST or None)
    if request.method == 'POST':

        if form.is_valid:
            exist = User.objects.filter(
                username=request.POST['correo']).count()

            if exist != 0:
                mensaje = f"El correo ingresado ya existe, por favor ingrese un nuevo correo."
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
                                           user_id=u.id,
                                           genero_id=request.POST['genero'],
                                           comuna_id=comuna.id,
                                           tipo_cliente_id=request.POST['tipo_cliente'])
                    return HttpResponseRedirect('/account/login/')

    return render(request, 'account/register.html', {'form': form, })


def logout_account(request):

    if request.user.is_authenticated:

        logout(request)
        return HttpResponseRedirect('/')
    return None
