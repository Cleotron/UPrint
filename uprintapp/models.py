from django.db import models

class Pyme:

    def __init__(self):
        self.huella = 0


    def calcularHuella(self,empleados, consumo_luz, consumo_agua, consumo_gas):
        # calculamos la huella de la pyme con el consumo que nos proporciona el usuario multiplicado por el factor
        h_luz = args[1]*0.001*0.505*12/args[0]
        h_agua = args[2]*1*6/args[0]
        h_gas=args[3]*11.7*12/args[0]

        huella = h_luz + h_agua + h_gas

        return huella, h_luz, h_agua, h_gas

    def mediaSector(sector):

        media_gas = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_gas'))
        media_agua = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_agua'))
        media_luz = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('kW'))

        media_sector = gas + agua + elect
        
        return media_sector*12, media_luz*12, media_agua*6, media_gas*12


class Pyme_DB(models.Model):

    raz_soc = models.TextField()
    giro = models.TextField()
    l_agua = models.FloatField()
    coste_agua = models.FloatField()
    kW = models.FloatField()
    coste_luz = models.FloatField()
    l_gas = models.IntegerField()
    coste_gas = models.FloatField()