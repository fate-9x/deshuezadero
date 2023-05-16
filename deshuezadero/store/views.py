from django.shortcuts import *
from appDeshuezadero.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import *
# Create your views here.


def store_repuestos(request):

    productos = Repuesto.objects.all()

    return render(request, 'store/store_repuestos.html', {'productos': productos})


def store_autos(request):

    autos = Auto.objects.all()

    return render(request, 'store/store_autos.html', {'autos': autos})


def repuestoView(request, id):

    producto = Repuesto.objects.filter(id=id)
    producto_fotos = RepuestoFotos.objects.filter(
        repuesto_id=producto.get().id)

    return render(request, 'store/product.html', {'producto': producto.get(), 'producto_fotos': producto_fotos.get()})


def autoView(request, id):
    auto = Auto.objects.filter(id=id)
    auto_fotos = AutoFotos.objects.filter(auto_id=id)

    return render(request, 'store/auto.html', {'auto': auto.get(), 'auto_fotos': auto_fotos.get()})


def createCart(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            try:
                if request.POST['modelo'] != None:
                    auto = Auto.objects.filter(
                        id=request.POST['id']).get()

                    try:
                        item = Carrito.objects.filter(
                            auto_id=request.POST['id'], user_id=request.user.id)

                        if item.count() > 0:
                            return HttpResponseRedirect('/store/cart/')

                        else:
                            Carrito.objects.create(
                                cantidad=1, auto_id=request.POST['id'], user_id=request.user.id, precio=auto.precio, suma=auto.precio, nombre=request.POST['modelo'])

                        return HttpResponseRedirect('/store/cart/')

                    except Carrito.DoesNotExist:

                        Carrito.objects.create(
                            cantidad=1, auto_id=request.POST['id'], user_id=request.user.id, precio=auto.precio, suma=auto.precio, nombre=request.POST['modelo'])
                        return HttpResponseRedirect('/store/cart/')
            except Exception as e:

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

                    return HttpResponseRedirect('/store/cart/')

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


def form_auto(request):

    if request.user.is_authenticated:

        form = Formulario_Auto(request.POST, request.FILES or None)
        if request.method == 'POST':

            if form.is_valid:

                try:

                    auto = Auto.objects.filter(
                        vendedor_id=request.user.id, modelo=request.POST['modelo'], color=request.POST['color'], vin=request.POST['vin'])

                    print(auto.count())
                    if auto.count() > 0:

                        return HttpResponseRedirect('/')
                    else:
                        auto = request.POST
                        r = Auto.objects.create(
                            marca=auto['marca'], modelo=auto['modelo'], precio=auto['precio'], vin=auto['vin'], color=auto['color'], vendedor_id=request.user.id)

                        AutoFotos.objects.create(
                            foto=request.FILES.get('foto'), auto_id=r.id)

                        return HttpResponseRedirect('/store/autos/')

                except Auto.DoesNotExist:

                    auto = request.POST
                    r = Auto.objects.create(
                        marca=auto['marca'], modelo=auto['modelo'], precio=auto['precio'], vin=auto['vin'], color=auto['color'], vendedor_id=request.user.id)

                    AutoFotos.objects.create(
                        foto=request.FILES.get('foto'), auto_id=r.id)

                return HttpResponseRedirect('/store/repuestos/')

        return render(request, 'store/form_autos.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def crudProductos(request):

    repuestos = Repuesto.objects.filter(vendedor_id=request.user.id)

    autos = Auto.objects.filter(vendedor_id=request.user.id)

    return render(request, 'store/crud_productos.html', {'repuestos': repuestos, 'autos': autos})


def deleteAuto(request, auto_id):
    try:
        auto = Auto.objects.filter(
            id=auto_id, vendedor_id=request.user.id).delete()

        AutoFotos.objects.filter(auto_id=auto.id).delete()
    except Exception as e:

        auto = Auto.objects.filter(
            id=auto_id, vendedor_id=request.user.id)

        Carrito.objects.filter(auto_id=auto.get().id).delete()

        try:
            AutoFotos.objects.filter(
                auto_id=auto.get().id).delete()

            auto.delete()
            HttpResponseRedirect('/store/crud-productos/')

        except AutoFotos.DoesNotExist:
            HttpResponseRedirect('/store/crud-productos/')

    return HttpResponseRedirect('/store/crud-productos/')


def deleteRepuesto(request, producto_id):

    try:
        repuesto = Repuesto.objects.filter(
            id=producto_id, vendedor_id=request.user.id).delete()

        RepuestoFotos.objects.filter(repuesto_id=repuesto.id).delete()
    except Exception as e:

        repuesto = Repuesto.objects.filter(
            id=producto_id, vendedor_id=request.user.id)

        Carrito.objects.filter(producto_id=repuesto.get().id).delete()

        try:
            RepuestoFotos.objects.filter(
                repuesto_id=repuesto.get().id).delete()

            repuesto.delete()
            HttpResponseRedirect('/store/crud-productos/')

        except RepuestoFotos.DoesNotExist:
            HttpResponseRedirect('/store/crud-productos/')

    return HttpResponseRedirect('/store/crud-productos/')


def modificarRepuesto(request, producto_id):

    repuesto = Repuesto.objects.get(
        id=producto_id, vendedor_id=request.user.id)

    form = Formulario_Repuestos(request.POST, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid:

            rep = Repuesto.objects.filter(
                id=producto_id, vendedor_id=request.user.id).get()

            rep.nombre = request.POST['nombre']
            rep.precio = request.POST['precio']
            rep.stock = request.POST['stock']
            rep.tipo_repuesto_id = request.POST['tipo_repuesto']

            rep.save()

            rep_foto = RepuestoFotos.objects.filter(
                repuesto_id=producto_id).get()

            rep_foto.foto = request.FILES['foto']

            rep_foto.save()

            return HttpResponseRedirect('/store/repuestos/')

    return render(request, 'store/modificar_repuesto.html', {'repuesto': repuesto, 'form': form})


def modificarAuto(request, auto_id):
    auto = Auto.objects.get(
        id=auto_id, vendedor_id=request.user.id)

    form = Formulario_Auto(request.POST, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid:

            a = Auto.objects.filter(
                id=auto_id, vendedor_id=request.user.id).get()

            a.marca = request.POST['marca']
            a.modelo = request.POST['modelo']
            a.precio = request.POST['precio']
            a.vin = request.POST['vin']
            a.patente = request.POST['patente']
            a.color = request.POST['color']

            a.save()

            a_foto = AutoFotos.objects.filter(
                auto_id=auto_id).get()

            a_foto.foto = request.FILES['foto']

            a_foto.save()

            return HttpResponseRedirect('/store/autos/')

    return render(request, 'store/modificar_auto.html', {'auto': auto, 'form': form})
