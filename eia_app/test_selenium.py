"""
    Archivo para las pruebas realizadas en selenium
"""

from django.urls import reverse
from utils.testutils import SeleniumTestCase
from .models import DatosProyecto


class ViewsTest(SeleniumTestCase):
    """
        Clase para probar las vistas del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium",
            url="www.google.com.ve")
        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_proyecto(self):
        """
            Test para anadir datos de un proyecto.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector('#datos-proyectos').click()
        self.selenium.find_element_by_css_selector('#add').click()
        titulo = "Proyecto de prueba"
        self.selenium.find_element_by_name('titulo').send_keys(titulo)
        ubicacion = "Caracas, Venezuela"
        self.selenium.find_element_by_name('ubicacion').send_keys(ubicacion)
        area = "Ecologica"
        self.selenium.find_element_by_name('area').send_keys(area)
        tipo = "Recreación"
        self.selenium.find_element_by_name('tipo').send_keys(tipo)
        url = "https://www.google.co.ve"
        self.selenium.find_element_by_name('url').send_keys(url)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_ver_detalles_datosproyecto(self):
        """
            Probar el boton de ver detalles de un datosproyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_proyectos/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.proyecto.id)).click()

    def test_editar_datosproyecto(self):
        """
            Editar los datos de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_proyectos/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.proyecto.id)).click()
        titulo = "Edicion de prueba"
        self.selenium.find_element_by_name('titulo').send_keys(titulo)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_datosproyecto(self):
        """
            Borrar los datos de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_proyectos/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.proyecto.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()
