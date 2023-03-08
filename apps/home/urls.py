from django.urls import path

from .views import *

urlpatterns = [
  path('',index,name='index'),
  path('f2/',home,name='home')
]

