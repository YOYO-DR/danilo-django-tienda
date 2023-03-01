from django.http import HttpResponse


def index(request):
    return HttpResponse("""<h1 
    style='font-family: sans-serif;
    color:red;
    display:flex;
    justify-content:center;
    align-items:center;
    width:100%;
    height:100%;'>
    Hola Yoiner, esta es la vista del home.</h1>""")

def home(request):
    return HttpResponse("""<h1 style='font-family: sans-serif;
    color:green;
    display:flex;
    justify-content:center;
    align-items:center;
    width:100%;
    height:100%;'>
    Hola Yoiner, esta es una funcion del home.</h1>""")
