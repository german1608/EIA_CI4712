"""
Utilities para las pruebas unitarias y de comportamiento
del proyecto
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class SeleniumTestCase(StaticLiveServerTestCase):
    """
    Clase para crear casos de pruebas que usen selenium
    """
    fixtures = ['groups.json', 'users.json']
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.selenium.quit()
