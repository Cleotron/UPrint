from django.db import models

class Pyme:

    def __init__(self):
        self.huella = 0
    def calcularHuella(self,args):
        # calculamos la huella de la pyme
        huella = self.huella
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
    