from django.shortcuts import *
from appDeshuezadero.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
# Create your views here.


def store(request):

    productos = Repuesto.objects.all()

    return render(request, 'store/store.html', {'productos': productos})


def product(request, id):

    producto = Repuesto.objects.get(id=id)

    return render(request, 'store/product.html', {'producto': producto})


def createCart(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            datos = Repuesto.objects.filter(id=request.POST['id']).get()
            try:

                producto = Carrito.objects.get(
                    producto_id=request.POST['id'],
                    user_id=request.user.id
                )

                producto.cantidad = int(producto.cantidad) + \
                    int(request.POST['cantidad'])
                producto.save()

            except Carrito.DoesNotExist:
                Carrito.objects.create(
                    cantidad=request.POST['cantidad'], producto_id=request.POST['id'], user_id=request.user.id, precio=datos.precio, suma=int(datos.precio) * int(request.POST['cantidad']), nombre=request.POST['nombre'])

            return HttpResponseRedirect('/store/cart/')
    return HttpResponseRedirect('/')


def deleteCart(request, producto_id):
    Carrito.objects.filter(user_id=request.user.id,
                           producto_id=producto_id).delete()

    return HttpResponseRedirect('/store/cart/')


def cart(request):

    if request.user.is_authenticated:

        carrito = Carrito.objects.filter(user_id=request.user.id)

        return render(request, 'store/cart.html', {'carrito': carrito})
    return HttpResponseRedirect('/')
