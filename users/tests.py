"""
Pruebas unitarias del modulo de usuarios de EIA
"""
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from selenium import webdriver
from .models import Usuario


class UserTestCase(StaticLiveServerTestCase):
    ''' Clase que contiene las pruebas unitarias'''

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(UserTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(UserTestCase, self).tearDown()

    def test_registered_user(self):
        ''' Caso de prueba que hae post de un formulario de registro con datos, y verifica que se
            agrego el usua  rio a la base de datos.'''

        selenium = self.selenium
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get(self.live_server_url+'/users/create/')
        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        doc_identidad = selenium.find_element_by_id('id_doc_identidad')

        submit = selenium.find_element_by_id('registrar')

        #Fill the form with data
        first_name.send_keys('Jean')
        last_name.send_keys('Guzman')
        username.send_keys('jguzman')
        email.send_keys('jguzman@qawba.com')
        password1.send_keys('123456q7q7')
        password2.send_keys('123456q7q7')
        doc_identidad.send_keys('V-90')

        #submitting the form
        submit.submit()
        time.sleep(1)

        user = (Usuario.objects.get(username='jguzman'))
        self.assertEqual(user.first_name, 'Jean')

    def test_display_no_created_user(self):
        ''' Caso que intenta editar la informacion de un usuario inexistente,
        comprueba que recibe respuesta 404'''
        test_user = Usuario.objects.create(username="jguzman",
                                           password="contrasenaSecreta",
                                           first_name="Jean",
                                           last_name="Guzman",
                                           email="jguzman@gmail.com",
                                           doc_identidad=10)
        response = self.client.get(
            reverse('edit_user', kwargs={'pk': test_user.pk+1}))
        self.assertEqual(response.status_code, 404)

# Create your tests here.
# pylint: disable=no-self-use
class TestUsuarioModel(TestCase):
    """
    Pruebas para el modelo de usuarios. Las pruebas encapsulan:
    * Creacion de usuarios
    * Decirle a Django que use esta tabla en vez de la que trae por defecto
    """
    def setUp(self):
        self.usuario = Usuario.objects.create_user('username',
                                                   'username@username.com',
                                                   'password',
                                                   first_name='Usuario',
                                                   last_name='De Prueba')

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

    def test_model_full_name(self):
        """ El nombre completo se obtiene al concatenar el nombre y el apellido """
        actual = self.usuario.full_name()
        expected = self.usuario.first_name + ' ' + self.usuario.last_name
        self.assertEqual(actual, expected)
