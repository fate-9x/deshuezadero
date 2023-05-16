from django.urls import path
from .views import *

urlpatterns = [
    path('repuestos/', store, name='store_repuestos'),
    path('form-repuestos/', form_repuestos, name='form_repuestos'),
    path('cart/', cart, name='store_cart'),
    path('checkout/', checkout, name='checkout'),
    path('product/<int:id>', product, name='store_product'),
    path('create-cart/', createCart, name='create_cart'),
    path('delete-item-cart/<int:producto_id>',
         deleteCart, name='delete_product'),
    path('crud-repuestos/',
         crudRepuestos, name='crud_repuestos'),
    path('delete-repuesto/<int:producto_id>/',
         deleteRepuesto, name='delete_repuesto'),
    # path('crud-repuestos/',
    #      crudRepuestos, name='crud_repuestos'),


]
