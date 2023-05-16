from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('transaction/', transaction, name='transaction'),
    path('crear_pago/', create_payment, name='crear_pago'),
]
