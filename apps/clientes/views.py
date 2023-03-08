from django.shortcuts import render

def clientes(request):
    context = {'clientes':['Yoiner','Daniel','Breynner','Aleja','Donovan']}
    return render(request,'clientes.html',context)