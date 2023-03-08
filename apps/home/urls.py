from django.urls import path
from apps.home.views import *

urlpatterns = [
    path('',index,name='index'),
    path('funcion/',home,name='funcion')
]