from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='font-family:sans-serif; color: red;width: 100%;height:100%;display:flex;justify-content:center;align-items:center'>Hola Yoiner, me encuetro en la aplicacion de Home.</h1>")

def home(request):
    return HttpResponse("<h1 style='font-family:sans-serif; color: red;'>Hola Yoiner, Esto es una nueva funcion de home.</h1>")