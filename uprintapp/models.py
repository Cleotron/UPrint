from django.db import models

class Pyme:

    def __init__(self):
        self.huella = 0


    def calcularHuella(self,args):
        # calculamos la huella de la pyme con el consumo que nos proporciona el usuario multiplicado por el factor
        huella = args[0]*1 + args[1]*1 + args[2]*1

        return huella


class Pyme_DB(models.Model):

    raz_soc = models.TextField()
    giro = models.TextField()
    l_agua = models.FloatField()
    coste_agua = models.FloatField()
    kW = models.FloatField()
    coste_luz = models.FloatField()
    l_gas = models.IntegerField()
    coste_gas = models.FloatField()
    