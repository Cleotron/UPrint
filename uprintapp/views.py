from django.shortcuts import render
from clientesapp.models import Cliente
from datetime import datetime

def index(request):
    # Esta es la home, donde ofrecemos algo de informacion sobre la huella de carbono
    return render(request, "home.html")

def consultaPyme(request):
    name = request.POST['name']
    tipo = request.POST['loc']

    consumo_luz = request.POST['luz']
    consumo_agua = request.POST['agua']
    consumo_gas = request.POST['gas']
    #con el numero de empleados podemos saber el tipo de empresa (micro, pequeña, mediana, gran empresa)
    empleados = request.POST['empleados']
    sector = request.POST['sector']

    args = (consumo_luz, consumo_agua, consumo_gas, empleados, sector)

    pyme = Pyme()
    reg = pyme.calcularHuella(args)
    contexto = {
        'resultado': reg,
        'alta': datetime.now()
    }
    return render(request, "clientes/conf-alta.html", contexto)


def huellaPyme():
    pass