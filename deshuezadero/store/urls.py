from django.urls import path
from .views import *

urlpatterns = [
    path('store', store, name='store_index'),
]