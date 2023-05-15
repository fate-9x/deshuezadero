from django.urls import path
from .views import *

urlpatterns = [
    path('login/', formulario_login, name='formulario_login'),
    path('register/', formulario_register, name='formulario_register'),
    path('logout/', logout_account, name='logout'),

]
