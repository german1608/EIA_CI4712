'''
Pruebas unitarias de las vistas del modulo de medidas
'''
from django.shortcuts import reverse
from django.test import TestCase, tag
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

    def test_login_required(self):
        '''
        Prueba que la vista sea solamente accedible por usuarios
        autenticados
        '''
        login_url = reverse('login')
        target_url = reverse('medidas:lista-medidas')
        response = self.client.get(target_url)
        actual = response
        expected = login_url + '?next=' + target_url
        self.assertRedirects(actual, expected, msg_prefix='La vista de listado de medidas no requiered login')
