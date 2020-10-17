from django.shortcuts import render
from uprintapp.models import Pyme
from datetime import datetime

def index(request):
    # Esta es la home, donde ofrecemos algo de informacion sobre la huella de carbono
    return render(request, "home.html")

def formulario(request):
    # Esta es la home, donde ofrecemos algo de informacion sobre la huella de carbono
    return render(request, "pymes/form-pymes.html")

def consultaPyme(request):
    name = request.POST['name']
    empleados = request.POST['empleados']
    sector = request.POST['sector']

    consumo_luz = request.POST['luz']
    consumo_agua = request.POST['agua']
    consumo_gas = request.POST['gas']
    #con el numero de empleados podemos saber el tipo de empresa (micro, pequeña, mediana, gran empresa)

    args = (name, empleados, sector, consumo_luz, consumo_agua, consumo_gas)

    pyme = Pyme()
    huella = pyme.calcularHuella(args)
    contexto = {
        'resultado': huella,
        'alta': datetime.now()
    }
    return render(request, "pymes/huella.html", contexto)

