'''
Pruebas unitarias de las vistas del modulo de medidas
'''
from django.shortcuts import reverse
from django.test import TestCase, tag
from medidas.models import Medida
from medidas.views import MedidaListView, MedidaDetailView


class MedidaViewHelper(TestCase):
    '''
    Helper para las pruebas de las vistas de medidas
    '''
    fixtures = ['users-and-groups.json', 'medidas.json']

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
    target_url = reverse('medidas:lista-medidas')

    def test_url_view_correspondence(self):
        '''
        Prueba que el url de listado de medidas use la vista
        MedidaListView
        '''
        self.login()
        response = self.client.get(self.target_url)
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
        response = self.client.get(self.target_url)
        actual = response
        expected = login_url + '?next=' + self.target_url
        self.assertRedirects(actual, expected, msg_prefix='La vista de listado de medidas no requiered login')

    def test_contexto_tiene_lista(self):
        '''
        Prueba que verifica que el contexto tenga la lista de medidas
        '''
        self.login()
        response = self.client.get(self.target_url)
        actual = response.context['object_list']
        expected = Medida.objects.all()
        self.assertEqual(list(actual), list(expected), 'La lista de medidas no es correcta')

    def test_template_correcto(self):
        ''' Prueba que el template usado por el listado sea medidas/list.html '''
        # Nos logueamos
        self.login()
        response = self.client.get(self.target_url)
        actual = response
        expected = 'medidas/list.html'
        self.assertTemplateUsed(actual, expected)

@tag('medida')
class MedidaDetailViewTestCase(MedidaViewHelper):
    '''
    Pruebas unitarias para la vista de detalles de medidas
    '''
    def test_url_view_correspondence(self):
        ''' Prueba que el url para los detalles tenga como vista MedidaDetailView '''
        self.login()
        medida = Medida.objects.get(nomenclatura='MED-1')
        target_url = reverse('medidas:detalles-medida', kwargs={'pk': medida.pk})
        response = self.client.get(target_url)
        actual = response.resolver_match.func.__name__
        expected = MedidaDetailView.as_view().__name__
        self.assertEqual(actual, expected, 'La vista de detalles de medidas'
                                           'no es MedidaDetailView')

