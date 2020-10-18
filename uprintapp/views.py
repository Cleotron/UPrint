from django.shortcuts import render
from uprintapp.models import Pyme
from datetime import datetime
from django.db.models import Avg

def index(request):
    # Esta es la home, donde ofrecemos algo de informacion sobre la huella de carbono
    return render(request, "home.html")

def formulario(request):
    # Esta es la home, donde ofrecemos algo de informacion sobre la huella de carbono
    return render(request, "pymes/form-pymes.html")

def consultaPyme(request):
    sector = request.POST['sector']
    empleados = request.POST['empleados']
    sector = request.POST['sector']

    consumo_luz = request.POST['luz']
    consumo_agua = request.POST['agua']
    consumo_gas = request.POST['gas']
    #con el numero de empleados podemos saber el tipo de empresa (micro, pequeña, mediana, gran empresa)

    #args = (empleados, sector, consumo_luz, consumo_agua, consumo_gas)

    pyme = Pyme()
    (huella, h_luz, h_agua, h_gas) = pyme.calcularHuella(empleados, consumo_luz, consumo_agua, consumo_gas)
    (media_sector, media_luz, media_agua, media_gas) = pyme.mediaSector(sector)


    contexto = {
        'resultado': huella,
        'huella_luz':h_luz,
        'huella_agua':h_agua,
        'huella_gas':h_gas,
        'media_sector': media_sector,
        'sector_luz': media_luz,
        'sector_agua': media_agua,
        'sector_gas': media_gas,

    }
    return render(request, "pymes/huella.html", contexto)

