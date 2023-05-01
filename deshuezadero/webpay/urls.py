from django.urls import path
from .views import *

urlpatterns = [
    path('crear_pago/', create_payment, name='crear_pago'),
]