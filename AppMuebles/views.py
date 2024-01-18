from django.shortcuts import render
from AppMuebles.forms import SurForm, NorteForm, CentroForm
from AppMuebles.models import Sur, Norte, Centro

def inicio(request):
    return render(request, "AppMuebles/inicio.html")

def viaje_sur(request):
    return render(request, "AppMuebles/sur.html")

def viaje_norte(request):
    return render(request, "AppMuebles/norte.html")

def viaje_centro(request):
    return render(request, "AppMuebles/centro.html")

def agregar_viajesur(request):
    if request.method == "POST":
        nuevo_formulario = SurForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data #lo volvemos diccionario
            sur_nuevo = Sur(lugar=info["lugar"], descripcion=info["descripcion"], precio=info["precio"])
            sur_nuevo.save() #lo guarda en la base de datos
            return render(request, "AppMuebles/inicio.html") #nos devuelve a inicio con los datos guardados
    else:
            nuevo_formulario = SurForm() #morstar formulario vacio
    return render(request, "AppMuebles/agregarviajesur.html", {"mi_formu":nuevo_formulario})

def agregar_viajecentro(request):
    if request.method == "POST":
        nuevo_formulario = CentroForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data
            centro_nuevo = Centro(lugar=info["lugar"], descripcion=info["descripcion"], precio=info["precio"])
            centro_nuevo.save()
            return render(request, "AppMuebles/inicio.html")
    else:
            nuevo_formulario = CentroForm()
    return render(request, "AppMuebles/agregarviajecentro.html", {"mi_formu":nuevo_formulario})

def agregar_viajenorte(request):
    if request.method == "POST":
        nuevo_formulario = NorteForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data
            norte_nuevo = Norte(lugar=info["lugar"], descripcion=info["descripcion"], precio=info["precio"])
            norte_nuevo.save()
            return render(request, "AppMuebles/inicio.html")
    else:
            nuevo_formulario = NorteForm() 
    return render(request, "AppMuebles/agregarviajenorte.html", {"mi_formu":nuevo_formulario})