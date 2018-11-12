"""
Pruebas unitarias del dashboard de EIA
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from users.models import Usuario
from .views import DashboardView

# Create your tests here.
# pylint: disable=no-self-use
class TestViews(TestCase):
    """
    Pruebas unitarias para las vistas de la aplicacion `dashboard`
    """
    def setUp(self):
        """
        Configuracion necesaria para cada prueba del suite.
        Crea un usuario para poder probar autenticacion en la plataforma
        """
        Usuario.objects.create_user('username', email='username@username.com',
                                    password='password', doc_identidad='12345',
                                    first_name='Nombre', last_name='Apellido')
        self.client = Client()

    def test_dashboard_existence(self):
        """ Prueba la existencia de la clase que muestra el dashboard """
        DashboardView.as_view()

    def test_url_existence(self):
        """ Prueba la existencia del url que apunta a la vista DashboardView """
        reverse('dashboard:index')

    def test_login_required(self):
        """ Prueba que la vista requiera el inicio de sesion """

        # Hacemos la peticion sin estar autenticados
        response = self.client.get(reverse('dashboard:index'))
        self.assertRedirects(response, '{}?next={}'.format(settings.LOGIN_URL,
                                                           reverse('dashboard:index')))

        # Nos logueamos
        self.client.login(username='username', password='password')
        response = self.client.get(reverse('dashboard:index'))
        # Verificamos que no redirija y que el nombre de la funcino
        # que maneja la peticion sea el correcto
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__,
                         DashboardView.as_view().__name__)
        self.client.logout()
