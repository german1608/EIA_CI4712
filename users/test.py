
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Usuario
import time


class UserTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(UserTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(UserTestCase, self).tearDown()

    '''def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/users/create/')
        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_id('register')

        #Fill the form with data
        first_name.send_keys('Yusuf')
        last_name.send_keys('Unary')
        username.send_keys('unary')
        email.send_keys('yusuf@qawba.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result'''

    def test_registered_user(self):
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

        user=(Usuario.objects.get(username='jguzman'))
        self.assertEqual(user.first_name, 'Jean')


    def test_display_no_created_user(self):
        test_user = Usuario.objects.create(username="jguzman", password="contrasenaSecreta", first_name="Jean", last_name="Guzman", email="jguzman@gmail.com", doc_identidad=10)
        selenium = self.selenium
        response = self.client.get(reverse('edit_user', kwargs={'pk':test_user.pk+1}))
        self.assertEqual(response.status_code, 404)