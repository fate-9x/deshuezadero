from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from appDeshuezadero.models import *

# Create your views here.


def home(request):

    return render(request, 'home/index.html', {})
