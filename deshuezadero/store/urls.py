from django.urls import path
from .views import *

urlpatterns = [
    path('repuestos/', store_repuestos, name='store_repuestos'),
    path('autos/', store_autos, name='store_autos'),

    path('form-repuestos/', form_repuestos, name='form_repuestos'),
    path('form-autos/', form_auto, name='form_autos'),

    path('cart/', cart, name='store_cart'),

    path('repuesto/<int:id>', repuestoView, name='store_product'),
    path('auto/<int:id>', autoView, name='store_auto'),

    path('create-cart/', createCart, name='create_cart'),

    path('crud-productos/',
         crudProductos, name='crud_repuestos'),

    path('delete-item-cart/<int:producto_id>',
         deleteCart, name='delete_product'),
    path('delete-repuesto/<int:producto_id>/',
         deleteRepuesto, name='delete_repuesto'),
    path('delete-auto/<int:auto_id>/',
         deleteAuto, name='delete_auto'),

    path('modificar-repuesto/<int:producto_id>/',
         modificarRepuesto, name='modificar_repuesto'),
    path('modificar-auto/<int:auto_id>/',
         modificarAuto, name='modificar_auto'),




]
