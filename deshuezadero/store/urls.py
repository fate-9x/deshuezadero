from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name='store_index'),
    path('cart/', cart, name='store_cart'),
    path('checkout/', store, name='store_index'),
    path('product/<int:id>', product, name='store_product'),
    path('create-cart/', createCart, name='create_cart'),
    path('delete-product/<int:producto_id>',
         deleteCart, name='delete_product'),

]
