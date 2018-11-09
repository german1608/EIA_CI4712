
"""
    TestCase para el modulo de usuarios del proyecto EIA
"""

import time
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from .models import Usuario


class UserTestCase(LiveServerTestCase):
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
        doc_identidad.send_keys(90)

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
        response = self.client.get(reverse('edit_user', kwargs={'pk':test_user.pk+1}))
        self.assertEqual(response.status_code, 404)
