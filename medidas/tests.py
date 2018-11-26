'''
Pruebas unitarias del modulo de medidas
'''
from django.test import TestCase
from django.forms.models import model_to_dict
from .forms import MedidaForm
from .models import Medida

# Create your tests here.
class MedidaFormTestCase(TestCase):
    ''' Pruebas unitarias para el formulario de medida '''
    fixtures = ['medidas.json']

    def setUp(self):
        self.medida = Medida.objects.get(nombre='Medida 1')
        self.medida_dict = model_to_dict(self.medida)

    def test_form_existence(self):
        ''' Test de existencia de MedidaForm '''
        MedidaForm()

    def test_form_nomenclatura_not_empty(self):
        ''' Prueba para validar la nomenclatura '''
        self.medida_dict['nomenclatura'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(form.is_valid(), 'El formulario no debe estar valido sin la nomenclatura')
