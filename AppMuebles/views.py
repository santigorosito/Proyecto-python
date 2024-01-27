from django.shortcuts import render
from AppMuebles.forms import SurForm, NorteForm, CentroForm, RegistrarUser, EditarUser
from AppMuebles.models import Sur, Norte, Centro
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, "AppMuebles/inicio.html")

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = info["username"]
            contra = info["password"]
            usuario_actual = authenticate(username=usuario, password=contra)
            if usuario_actual is not None: #si el usuario actual es "algo" (encontro un usuario)
                login(request, usuario_actual) #iniciar sesion con este usuario
                return render(request, "AppMuebles/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else: #no encuentra al usuario
                return render(request, "AppMuebles/inicio.html", {"mensaje":"Error, datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "registro/inicio_sesion.html", {"formu":form})

def cerrar_sesion(request):
    logout(request)
    return render(request, "registro/cerrar_sesion.html")

def registro(request): 
    if request.method == "POST":
        formulario = RegistrarUser(request.POST) #la info del registro
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = info["username"]
            formulario.save()
            return render(request, "AppMuebles/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
    else:
        formulario = RegistrarUser()
    return render(request, "registro/register_user.html", {"formu":formulario})

def editar_perfil(request):
    usuario_actual = request.user
    if request.method == "POST":
        formulario = EditarUser(request.POST) #la info del registro
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario_actual.username = info["usuario"]
            usuario_actual.set_pasword(info["password1"])
            usuario_actual.save()
            return render(request, "AppMuebles/inicio.html")
    else:
        formulario = EditarUser(initial={"usuario":usuario_actual.username,
                                            "contraseña":usuario_actual.password})
    return render(request, "registro/editar_user.html", {"formu":formulario})


def busqueda_viaje(request):
    return render(request, "AppMuebles/buscar_viaje.html")


# def viaje_sur(request):
    return render(request, "AppMuebles/sur.html")

# def viaje_sur(request):
    via_sur = Sur.objects.all()
    info = {"sur1":via_sur}
    return render(request, "AppMuebles/sur.html", info)#

# def agregar_viajesur(request):
    if request.method == "POST":
        nuevo_formulario = SurForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data #lo volvemos diccionario
            sur_nuevo = Sur(lugar=info["lugar"], descripcion=info["descripcion"], precio=info["precio"])
            sur_nuevo.save() #lo guarda en la base de datos
            return render(request, "AppMuebles/inicio.html") #nos devuelve a inicio con los datos guardados
    else:
            nuevo_formulario = SurForm() #morstar formulario vacio
    return render(request, "AppMuebles/agregarviajesur.html", {"mi_formu":nuevo_formulario})#

# def actualizar_sur(request, sur_id):
    viaje_escogido= Sur.objects.get(lugar=sur_id)
    if request.method == "POST":
        nuevo_formulario = SurForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data #lo volvemos diccionario
            viaje_escogido.lugar= info["lugar"]
            viaje_escogido.descripcion= info["descripcion"]
            viaje_escogido.precio= info["precio"]
            viaje_escogido.save() #lo guarda en la base de datos
            return render(request, "AppMuebles/inicio.html") #nos devuelve a inicio con los datos guardados
    else:
            nuevo_formulario = SurForm(initial={"lugar":viaje_escogido.lugar, "descripcion":viaje_escogido.descripcion, "precio":viaje_escogido}) #morstar formulario vacio
    return render(request, "AppMuebles/update_sur.html", {"mi_formu":nuevo_formulario})#

# def eliminar_viaje_sur(request, sur_id):
    viaje_escogido= Sur.objects.get(lugar=sur_id)
    viaje_escogido.delete()
    return render(request, "AppMuebles/sur.html")

#---------------------------------------------------------------------------------------------------------------------------------------------------#


# def viaje_norte(request):
    return render(request, "AppMuebles/norte.html")

# def viaje_norte(request):
    via_norte = Norte.objects.all()
    info = {"norte1":via_norte}
    return render(request, "AppMuebles/norte.html", info)

# def agregar_viajenorte(request):
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

# def actualizar_norte(request, norte_id):
    viaje_escogido2= Norte.objects.get(lugar=norte_id)
    if request.method == "POST":
        nuevo_formulario = NorteForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data #lo volvemos diccionario
            viaje_escogido2.lugar= info["lugar"]
            viaje_escogido2.descripcion= info["descripcion"]
            viaje_escogido2.precio= info["precio"]
            viaje_escogido2.save() #lo guarda en la base de datos
            return render(request, "AppMuebles/inicio.html") #nos devuelve a inicio con los datos guardados
    else:
            nuevo_formulario = NorteForm(initial={"lugar":viaje_escogido2.lugar, "descripcion":viaje_escogido2.descripcion, "precio":viaje_escogido2}) #morstar formulario vacio
    return render(request, "AppMuebles/update_norte.html", {"mi_formu2":nuevo_formulario})

# def eliminar_viaje_norte(request, norte_id):
    viaje_escogido2= Norte.objects.get(lugar=norte_id)
    viaje_escogido2.delete()
    return render(request, "AppMuebles/norte.html")

#------------------------------------------------------------------------------------------------------------------------------------------------------#

# def viaje_centro(request):
    return render(request, "AppMuebles/centro.html")

# def viaje_centro(request):
    via_centro = Centro.objects.all()
    info = {"centro1":via_centro}
    return render(request, "AppMuebles/centro.html", info)

# def agregar_viajecentro(request):
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

# def actualizar_centro(request, centro_id):
    viaje_escogido3= Centro.objects.get(lugar=centro_id)
    if request.method == "POST":
        nuevo_formulario = CentroForm(request.POST)
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data #lo volvemos diccionario
            viaje_escogido3.lugar= info["lugar"]
            viaje_escogido3.descripcion= info["descripcion"]
            viaje_escogido3.precio= info["precio"]
            viaje_escogido3.save() #lo guarda en la base de datos
            return render(request, "AppMuebles/inicio.html") #nos devuelve a inicio con los datos guardados
    else:
            nuevo_formulario = CentroForm(initial={"lugar":viaje_escogido3.lugar, "descripcion":viaje_escogido3.descripcion, "precio":viaje_escogido3.precio}) #morstar formulario vacio
    return render(request, "AppMuebles/update_centro.html", {"mi_formu3":nuevo_formulario})

# def eliminar_viaje_centro(request, centro_id):
    viaje_escogido3= Centro.objects.get(lugar=centro_id)
    viaje_escogido3.delete()
    return render(request, "AppMuebles/centro.html")

#------------------------------------------------------------------------------------------------------------------------------------------#

def resultado_viaje(request):
    if request.method == "GET":
        viaje_pedido = request.GET["Viaje"]
        resultados_sur = Sur.objects.filter(lugar__icontains=viaje_pedido)
        resultados_norte = Norte.objects.filter(lugar__icontains=viaje_pedido)
        resultados_centro = Centro.objects.filter(lugar__icontains=viaje_pedido)
        resultados_viajes = list(resultados_sur) + list(resultados_norte) + list(resultados_centro)
    return render(request, "AppMuebles/buscar_viaje.html", {"viajes":resultados_viajes})

#CRUUD
class ListaSur(LoginRequiredMixin, ListView):
    model = Sur
    template_name = "AppMuebles/sur.html"

class CrearSur(CreateView):
    model = Sur
    template_name = "AppMuebles/agregarviajesur.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/sur/"

class ActualizarSur(UpdateView):
    model = Sur
    template_name = "AppMuebles/agregarviajesur.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/sur/"

class EliminarSur(DeleteView):
    model = Sur
    template_name = "AppMuebles/eliminar_sur.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/sur/"



class ListaNorte(LoginRequiredMixin, ListView):
    model = Norte
    template_name = "AppMuebles/norte.html"

class CrearNorte(CreateView):
    model = Norte
    template_name = "AppMuebles/agregarviajenorte.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/norte/"

class ActualizarNorte(UpdateView):
    model = Norte
    template_name = "AppMuebles/agregarviajenorte.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/norte/"

class EliminarNorte(DeleteView):
    model = Norte
    template_name = "AppMuebles/eliminar_norte.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/norte/"



class ListaCentro(LoginRequiredMixin, ListView):
    model = Centro
    template_name = "AppMuebles/centro.html"
    success_url = "/centro/"

class CrearCentro(CreateView):
    model = Centro
    template_name = "AppMuebles/agregarviajecentro.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/centro/"

class ActualizarCentro(UpdateView):
    model = Centro
    template_name = "AppMuebles/agregarviajecentro.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/centro/"

class EliminarCentro(DeleteView):
    model = Centro
    template_name = "AppMuebles/eliminar_centro.html"
    fields = ["lugar", "descripcion", "precio"]
    success_url = "/centro/"

@login_required
def sobre_mi(request):
    return render(request, "AppMuebles/sobreMi.html")