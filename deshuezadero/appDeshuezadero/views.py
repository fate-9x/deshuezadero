from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from appDeshuezadero.models import *

# Create your views here.


def home(request):

    repuestos = Repuesto.objects.all()

    autos = Auto.objects.all()

    return render(request, 'home/index.html', {'repuestos': repuestos, 'autos': autos})


def nosotros(request):

    return render(request, 'home/nosotros.html', {})
