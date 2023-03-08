from django.contrib import admin
from django.urls import path
from apps.clientes.views import *

app_name = 'clientes'

urlpatterns = [
  path('clientes/',clientes,name='clientesHome')
]