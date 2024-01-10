from django.http import HttpResponse
from django.template import Template, Context, loader
import random

def bienvenida(request):
    return HttpResponse("hello")

def inicio(request):
    #plantilla = loader.get_template("inicio.html")
    #aleatorio = random.randint(1,10)
    #info = {"numero":aleatorio}
    #plantilla = plantilla.render(info)
    f = open("C:/Users/Santiago/Downloads/python-goro/Proyecto1/Proyecto1/Templates/inicio.html")
    plantilla = Template(f.read())
    f.close()
    aleatorio = random.randint(1,100)
    info = {"numero":aleatorio}
    contexto = Context(info)
    plantilla = plantilla.render(contexto)

    return HttpResponse(plantilla)