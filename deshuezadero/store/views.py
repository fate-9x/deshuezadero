from django.shortcuts import *

# Create your views here.


def store(request):
    return render(request, 'store/store.html', {})


def cart(request):
    return render(request, 'store/cart.html', {})
