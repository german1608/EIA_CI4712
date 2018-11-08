"""
Pruebas unitarias del dashboard de EIA
"""
from django.test import TestCase, Client
from users.models import Usuario
from .views import DashboardView

# Create your tests here.
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

    def test_dashboard_existence(self): # pylint: disable=no-self-use
        """ Prueba la existencia de la clase que muestra el dashboard """
        DashboardView.as_view()
