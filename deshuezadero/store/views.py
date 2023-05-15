from django.shortcuts import *
from appDeshuezadero.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import *
# Create your views here.


def store(request):

    productos = Repuesto.objects.all()

    return render(request, 'store/store_repuestos.html', {'productos': productos})


def product(request, id):

    producto = Repuesto.objects.filter(id=id)
    producto_fotos = RepuestoFotos.objects.filter(
        repuesto_id=producto.get().id)

    print(producto_fotos.get().foto)

    return render(request, 'store/product.html', {'producto': producto.get(), 'producto_fotos': producto_fotos.get()})


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
                producto.suma = int(producto.cantidad) * int(datos.precio)
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


def form_repuestos(request):

    if request.user.is_authenticated:

        form = Formulario_Repuestos(request.POST, request.FILES or None)
        if request.method == 'POST':

            if form.is_valid:

                try:

                    repuesto = Repuesto.objects.filter(
                        vendedor_id=request.user.id, nombre=request.POST['nombre'])

                    RepuestoFotos.objects.create(
                        foto=request.FILES.get('foto'), repuesto_id=repuesto.get().id)

                    repuesto.stock = int(repuesto.stock) + \
                        int(request.POST['stock'])

                    repuesto.save()

                    return HttpResponseRedirect('/store/repuestos/')

                except Repuesto.DoesNotExist:
                    repuesto = request.POST
                    r = Repuesto.objects.create(
                        nombre=repuesto['nombre'], stock=repuesto['stock'], precio=repuesto['precio'], tipo_repuesto_id=repuesto['tipo_repuesto'], vendedor_id=request.user.id)

                    RepuestoFotos.objects.create(
                        foto=request.FILES.get('foto'), repuesto_id=r.id)

                    return HttpResponseRedirect('/store/repuestos/')

        return render(request, 'store/form_repuestos.html', {'form': form})

    else:
        return HttpResponseRedirect('/')
