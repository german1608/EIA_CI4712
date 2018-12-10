'''
Pruebas unitarias de las vistas del modulo de medidas
'''
from django.shortcuts import reverse
from django.test import TestCase, tag
from django.forms.models import model_to_dict
from medidas.models import Medida
from medidas.views import MedidaListView


class MedidaViewHelper(TestCase):
    '''
    Helper para las pruebas de las vistas de medidas
    '''
    fixtures = ['users-and-groups.json']

    def login(self):
        '''
        Helper para autenticarnos facilmente
        '''
        self.client.login(username='especialistaesia', password='jaja1234')


@tag('medida')
class MedidaListViewTestCase(MedidaViewHelper):
    '''
    Pruebas para la vista de listado de medidas
    '''

    def test_url_view_correspondence(self):
        '''
        Prueba que el url de listado de medidas use la vista
        MedidaListView
        '''
        self.login()
        target_url = reverse('medidas:lista-medidas')
        response = self.client.get(target_url)
        actual = response.resolver_match.func.__name__
        expected = MedidaListView.as_view().__name__
        self.assertEqual(actual, expected, 'La vista de listado de medidas no '
                                           'es MedidaListView')