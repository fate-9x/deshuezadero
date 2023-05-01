from django.shortcuts import *

# Create your views here.

def store(request):
    return render(request, 'store/store.html', {})
