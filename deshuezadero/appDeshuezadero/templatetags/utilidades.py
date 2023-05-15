from django import template
from appDeshuezadero.models import Carrito, Cliente


register = template.Library()


@register.filter(name="getCartCount")
def getCartCount(user_id):
    return Carrito.objects.filter(user_id=user_id).count()


@register.filter(name="getItemsCart")
def getItemsCart(user_id):
    return Carrito.objects.filter(user_id=user_id)


@register.filter(name="getItemsCount")
def getItemsCount(user_id):

    productos = Carrito.objects.filter(user_id=user_id)
    suma_cantidad = 0

    for producto in productos:
        suma_cantidad += int(producto.cantidad)

    return suma_cantidad


@register.filter(name="getSubTotal")
def getSubTotal(user_id):

    productos = Carrito.objects.filter(user_id=user_id)
    subtotal = 0

    for producto in productos:
        subtotal += int(producto.suma)

    return subtotal


@register.filter(name="getTipoCliente")
def getTipoCliente(user_id):

    cliente = Cliente.objects.filter(user_id=user_id).get()

    return cliente.tipo_cliente_id == 2
