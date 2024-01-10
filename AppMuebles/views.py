from django.shortcuts import render
from AppMuebles.models import Serie

def ver_serie(request):
    mis_series=Serie.objects.all()
    info = {"series":mis_series}
    return render(request, "AppMuebles/series.html", info)

def inicio(request):
    return render(request, "AppMuebles/inicio.html")