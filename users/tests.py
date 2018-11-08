"""
Pruebas unitarias del modulo de usuarios de EIA
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Usuario

# Create your tests here.
# pylint: disable=no-self-use
class TestUsuarioModel(TestCase):
    """
    Pruebas para el modelo de usuarios. Las pruebas encapsulan:
    * Creacion de usuarios
    * Decirle a Django que use esta tabla en vez de la que trae por defecto
    """
    def setUp(self):
        self.usuario = Usuario.objects.create_user('username', 'username@username.com', 'password')

    def test_model_existence(self):
        """ Verifica la existencia del modelo Usuario """
        Usuario()

    def test_model_conf(self):
        """ Verifica que el modelo por defecto sea el creado por nosotros """
        self.assertEqual(get_user_model(), Usuario,
                         'No se configuro correctamente la tabla de usuarios')

    def test_model_required_fields(self):
        """
        El usuario debe tener como campos:
        * email
        * first_name
        * last_name
        * username
        * password
        * doc_identidad
        """
        actual = Usuario.REQUIRED_FIELDS
        actual.sort()
        # password y username son implicitos
        esperado = ['first_name', 'last_name', 'email', 'doc_identidad']
        esperado.sort()
        self.assertEqual(actual, esperado)

    def test_model_str_representation(self):
        """ La representacion de un usuario deberia ser su nombre de usuario """
        self.assertEqual(str(self.usuario), self.usuario.email)
