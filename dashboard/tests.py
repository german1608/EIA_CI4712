"""
Pruebas unitarias del dashboard de EIA
"""
from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.conf import settings
from selenium.webdriver.firefox.webdriver import WebDriver
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


class TestDashboardInterface(StaticLiveServerTestCase):
    """
    Suite de pruebas para la interfaz del dashboard
    """
    fixtures = ['users-and-groups.json']
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        """
        Configuracion necesaria para cada prueba del suite.
        Crea un usuario para poder probar autenticacion en la plataforma
        """
        self.usuario = Usuario.objects.get(username='admin')

    def test_interface_content(self):
        """ Verificamos que el contenido de la interfaz sea el correcto """
        # Nos loggeamos
        self.selenium.get('{}{}'.format(self.live_server_url, reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

        # Obtenemos el contenido del elemento del side-menu
        nombre_usuario_input = self.selenium.find_element_by_id('side-menu-user-name')
        self.assertEqual(nombre_usuario_input.text, 'Bienvenido %s' % self.usuario.full_name())
