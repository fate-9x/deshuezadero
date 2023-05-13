from django.urls import path
from .views import *

urlpatterns = [
    path('store/', store, name='store_index'),
    path('cart/', cart, name='store_cart'),
    path('checkout/', store, name='store_index'),
]
