from django.db import models

class Pyme:

    def __init__(self):
        self.huella = 0


    def calcularHuella(self,args):
        # calculamos la huella de la pyme con el consumo que nos proporciona el usuario multiplicado por el factor
<<<<<<< Updated upstream
        h_luz = args[0]*0.001*0.505*12
        h_agua = args[1]*1*6
        h_gas=args[2]*11.7*12

        huella = h_luz + h_agua + h_gas

        return huella, h_luz, h_agua, h_gas

    def mediaSector(sector):

        media_gas = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_gas'))
        media_agua = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('l_agua'))
        media_luz = Pyme_DB.objects.filter(giro=sector).aggregate(Avg('kW'))

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
=======
        huella = args[0]*0.001*0.505 + args[1]*1 + args[2]*1

        return huella
"""
    def compararHuella(self, sector):
        self.huella
        #conectamos con la bd para comparar la huella de nuestra pyme con la media del sector
        connection = """
>>>>>>> Stashed changes


import cx_Oracle


class Consumo:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "password", "localhost/XE")

    def altaConsumo(self, args):
        cursor = self.connection.cursor()

        # name, empleados, sector, consumo_luz, consumo_agua, consumo_gas
        try:
            alta = ("INSERT INTO tabla VALUES(:p1, :p2, :p3, :p4, :p5, :p6)")
            cursor.execute(alta, args)
            reg = cursor.rowcount
            if reg>0:
                print("Hemos guardado sus datos correctamente")
                self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return reg
    