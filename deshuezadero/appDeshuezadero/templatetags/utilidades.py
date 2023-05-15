from django import template
from appDeshuezadero.models import Carrito


register = template.Library()


@register.filter(name="getCartCount")
def getCartCount(user_id):
    return Carrito.objects.filter(user_id=user_id).count()


@register.filter(name="getItemsCart")
def getItemsCart(user_id):
    return Carrito.objects.filter(user_id=user_id)
