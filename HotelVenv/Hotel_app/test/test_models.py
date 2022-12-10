from django.test import TestCase
from Hotel_app.models import *

class TestModels(TestCase):

    def testcreate(self):
        self.reservacionprueba = tblreservacion.objects.create(
            
            nombre = 'José',
            apellido = 'Perez',

            fecha_llegada = '2023-02-15',
            fecha_salida = '2022-02-20',
            email = 'josseperez@gmail.com',

            habitacion = 'Deluxe Double Room'


        )
