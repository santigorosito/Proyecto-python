from django.shortcuts import render

def inicio(request):
    return render(request, "AppMuebles/inicio.html")

def viaje_sur(request):
    return render(request, "AppMuebles/sur.html")

def viaje_norte(request):
    return render(request, "AppMuebles/norte.html")

def viaje_centro(request):
    return render(request, "AppMuebles/centro.html")