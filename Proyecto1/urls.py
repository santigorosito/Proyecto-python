"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppMuebles.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="Inicio"),

    #URLS de los modelos creados
    #path("sur/", viaje_sur, name="Sur"),#
    path("sur/", ListaSur.as_view(), name="Sur"),

    #path("norte/", viaje_norte, name="Norte"),#
    path("norte/", ListaNorte.as_view(), name="Norte"),

    #path("centro/", viaje_centro, name="Centro"),#
    path("centro/", ListaCentro.as_view(), name="Centro"),

    #path("form_sur/", agregar_viajesur, name="nuevo viaje S"),#
    path("form_sur/", CrearSur.as_view(), name="nuevo viaje S"),

    #path("form_centro/", agregar_viajecentro, name="nuevo viaje C"),#
    path("form_centro/", CrearCentro.as_view(), name="nuevo viaje C"),

    #path("form_norte/", agregar_viajenorte, name="nuevo viaje N"),#
    path("form_norte/", CrearNorte.as_view(), name="nuevo viaje N"),

    path("buscar_viaje/", busqueda_viaje),
    path("resultadoViajes/", resultado_viaje),

    #path("actualizarSur/<sur_id>", actualizar_sur, name="Actualizar Sur"),#
    path("actualizarSur/<int:pk>", ActualizarSur.as_view(), name="Actualizar Sur"),

    #path("actualizarNorte/<norte_id>", actualizar_norte, name="Actualizar Norte"),#
    path("actualizarNorte/<int:pk>", ActualizarNorte.as_view(), name="Actualizar Norte"),

    #path("actualizarCentro/<centro_id>", actualizar_centro, name="Actualizar Centro"),#
    path("actualizarCentro/<int:pk>", ActualizarCentro.as_view(), name="Actualizar Centro"),

    #path("eliminarViajeSur/<sur_id>", eliminar_viaje_sur, name="Eliminar Sur"),
    path("eliminarViajeSur/<int:pk>", EliminarSur.as_view(), name="Eliminar Sur"),

    #path("eliminarViajeNorte/<norte_id>", eliminar_viaje_norte, name="Eliminar Norte"),
    path("eliminarViajeNorte/<int:pk>", EliminarNorte.as_view(), name="Eliminar Norte"),

    #path("eliminarViajeCentro/<centro_id>", eliminar_viaje_centro, name="Eliminar Centro"),
    path("eliminarViajeCentro/<int:pk>", EliminarCentro.as_view(), name="Eliminar Centro"),

    path("login/", inicio_sesion, name="iniciar sesion"),
    path("signup/", registro, name="registrarse"),
    path("logout/", cerrar_sesion, name="cerrar sesion"),
    path("edit/", editar_perfil, name="editar perfil"),
    path("sobremi/", sobre_mi, name="Sobre mi"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)