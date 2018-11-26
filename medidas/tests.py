'''
Pruebas unitarias del modulo de medidas
'''
from django.test import TestCase
from .forms import MedidaForm
from .models import Medida

# Create your tests here.
class MedidaFormTestCase(TestCase):
    ''' Pruebas unitarias para el formulario de medida '''
    fixtures = ['medidas.json']

    def setUp(self):
        self.medida = Medida.objects.get(nombre='Medida 1')


    def test_form_existence(self):
        MedidaForm()
