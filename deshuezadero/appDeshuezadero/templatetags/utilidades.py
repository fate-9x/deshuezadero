from django import template
from appDeshuezadero.models import *


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


@register.filter(name="getFotoRepuesto")
def getFotoRepuesto(producto_id):

    fotos = RepuestoFotos.objects.filter(
        repuesto_id=producto_id)

    return fotos.get().foto


@register.filter(name="getTipoRepuesto")
def getTipoRepuesto(tipo_repuesto):

    tipo = TipoRepuesto.objects.filter(
        id=tipo_repuesto)

    return tipo.get().tipo
