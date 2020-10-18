from django.db import models

class Pyme:

    def __init__(self):
        self.huella = 0


    def calcularHuella(self,empleados, consumo_luz, consumo_agua, consumo_gas):
        # calculamos la huella de la pyme con el consumo que nos proporciona el usuario multiplicado por el factor
        h_luz = consumo_luz*0.505*12/empleados
        h_agua = consumo_agua*1*6/empleados
        h_gas=consumo_gas*11.7*12/empleados

        huella = h_luz + h_agua + h_gas

        return huella, h_luz, h_agua, h_gas

    def mediaSector(sector):

        media_gas = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_gas'))*11.7*12
        media_agua = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_agua'))*6
        media_luz = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('kW'))*0.001*0.505*12

        media_sector = gas + agua + elect
        
        return media_sector, media_luz, media_agua, media_gas


class Pyme_DB(models.Model):

    raz_soc = models.TextField()
    giro = models.TextField()
    l_agua = models.FloatField()
    coste_agua = models.FloatField()
    kW = models.FloatField()
    coste_luz = models.FloatField()
    l_gas = models.IntegerField()
    coste_gas = models.FloatField()