from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola, me encuetro en la aplicacion de Home.</h1>")