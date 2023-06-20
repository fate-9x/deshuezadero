from django.core.paginator import Paginator
from django.conf import settings
import os
import jwt
from appDeshuezadero.models import *


def formularioRegistroChoices():

    generos = []
    tipos_clientes = []

    for genero in Genero.objects.all():
        generos.append((genero.id, genero.nombre))

    for tipo_cliente in TipoCliente.objects.all():
        tipos_clientes.append((tipo_cliente.id, tipo_cliente.tipo))

    return generos, tipos_clientes


def formularioStoreChoices():
    tipos_repuestos = []

    for tipos in TipoRepuesto.objects.all():
        tipos_repuestos.append((tipos.id, tipos.tipo))

    return tipos_repuestos


def formularioReportesChoices():
    razones = []

    for razon in RazonesReportes.objects.all():
        razones.append((razon.id, razon.razon))

    return razones


def getToken(json):
    token = jwt.encode(json, settings.SECRET_KEY, algorithm='HS256')
    return token


def getItemsCart(user_id):
    carrito_count = Carrito.objects.filter(user_id=user_id).count()

    return carrito_count


def getComunas(region_id):

    comunas = Comuna.objects.filter(region_id=region_id)

    if comunas.count() > 0:
        return comunas


def get_paginacion(total, request):
    page = request.GET.get('page')
    paginator = Paginator(total, settings.TOTAL_PAGINAS)
    datos = paginator.get_page(page)
    numeros = []
    if len(datos) >= settings.TOTAL_PAGINAS:
        for ultima in range(1, datos.paginator.num_pages):
            numeros.append(ultima)
        numeros.append(ultima+1)

    return [datos, numeros, page]


def getExtension(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".png":
        return True
    elif extension == ".jpg":
        return True
    elif extension == ".jpeg":
        return True
    elif extension == ".JPG":
        return True
    elif extension == ".PNG":
        return True
    elif extension == ".JPEG":
        return True
    else:
        return False


def getExtensionSoloPdf(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".pdf":
        return True
    else:
        return False
