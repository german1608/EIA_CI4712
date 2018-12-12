'''
Pruebas unitarias de los forms del modulo de medidas
'''
from django.test import TestCase, tag
from django.forms.models import model_to_dict
from .forms import MedidaForm
from .models import Medida

# Create your tests here.
# pylint: disable=no-self-use


@tag('medida')
class MedidaFormTestCase(TestCase):
    ''' Pruebas unitarias para el formulario de medida '''
    fixtures = ['users-and-groups.json', 'medidas.json']

    def setUp(self):
        self.medida = Medida.objects.get(nombre='Medida 1')
        self.medida_dict = model_to_dict(self.medida)

    def test_form_existence(self):
        ''' Test de existencia de MedidaForm '''
        MedidaForm()

    def test_form_nomenclatura_not_empty(self):
        ''' Prueba para validar la nomenclatura requerida '''
        self.medida_dict['nomenclatura'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El formulario no debe estar valido sin la nomenclatura')

    def test_form_nomenclatura_max_length(self):
        ''' Prueba para validar la longitud maxima de la nomenclatura '''
        self.medida_dict['nomenclatura'] = 'f' * 11
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'La nomenclatura debe ser maximo 10 caracteres')

    def test_form_nombre_not_empty(self):
        ''' Prueba para validar que el nombre no sea vacio '''
        self.medida_dict['nombre'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El formulario no debe estar valido sin el nombre')

    def test_form_nombre_max_length(self):
        ''' Prueba para validar la longitud maxima del nombre '''
        self.medida_dict['nombre'] = 'f' * 101
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El nombre debe ser maximo 100 caracteres')

    def test_form_tipo_not_empty(self):
        ''' Prueba para validar que especifiquen un tipo '''
        self.medida_dict['tipo'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El tipo debe ser no vacio')

    def test_form_tipo_not_in_choices(self):
        ''' Prueba que solo especifiquen los valores adecuados en el tipo '''
        self.medida_dict['tipo'] = -1
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El tipo no esta en el rango valido [1,1]')
        self.medida_dict['tipo'] = 1
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El tipo no esta en el rango valido [1,1]')

    def test_form_medio_not_empty(self):
        ''' Prueba para validar que especifiquen un medio '''
        self.medida_dict['medio'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El medio debe ser no vacio')

    def test_form_medio_not_in_choices(self):
        ''' Prueba que solo especifiquen los valores adecuados para el medio '''
        self.medida_dict['medio'] = -1
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El medio no esta en el rango valido')
        self.medida_dict['medio'] = 3
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El medio no esta en el rango valido')

    def test_descripcion_not_empty(self):
        ''' Prueba que la descripcion no sea vacia '''
        self.medida_dict['descripcion'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'La descripcion no puede ser vacia')

    def test_marco_juridico_not_empty(self):
        ''' Prueba que el marco_juridico no sea vacia '''
        self.medida_dict['marco_juridico'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El marco_juridico no puede ser vacia')

    def test_area_not_empty(self):
        ''' Prueba que el area no sea vacia '''
        self.medida_dict['area'] = ''
        form = MedidaForm(self.medida_dict)
        self.assertFalse(
            form.is_valid(), 'El area no puede ser vacia')
