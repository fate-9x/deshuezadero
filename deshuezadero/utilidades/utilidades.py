from django.core.paginator import Paginator
from django.conf import settings
import os
import jwt
from appDeshuezadero.models import Carrito


def getToken(json):
    token = jwt.encode(json, settings.SECRET_KEY, algorithm='HS256')
    return token


def getItemsCart(user_id):
    carrito_count = Carrito.objects.filter(user_id=user_id).count()

    return carrito_count


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
