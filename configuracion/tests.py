"""
Pruebas Unitarias
"""
import time
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from selenium.webdriver.support.ui import Select
from configuracion.models import NIVEL_RELEVANCIA, TIPO_RELEVANCIA, GRADO_PERTUBACION
from configuracion.views import _calcular_via
from configuracion.forms import EstudioForm
from configuracion.models import Estudio
from utils.testutils import SeleniumTestCase

class KaraotaTests(TestCase):
    """
    Django Test
    """

    def setUp(self):
        """
        SetUp
        """
        self.client = Client() #Pruebas con testing tools de django

    def tearDown(self):
        """
        teardown
        """
        self.client = None

    def test_ponderaciones_iguala101(self):
        """
        test_ponderacionesigual101
        """
        valores = {
            'nombre': 'Nombre 1',
            'tipo': 'FS',
            'valoracion_relevancia': 'MA',
            'tipo_relevancia': 'DI',
            # 'intensidad': intensidad,
            # 'extension': extension,
            # 'duracion': duracion,
            # 'reversibilidad': reversibilidad,
            # 'probabilidad': probabilidad,
            'pondIntensidad': 21,
            'pondExtension': 20,
            'pondDuracion': 20,
            'pondReversibilidad': 20,
            'pondProbabilidad': 20,
            # 'via': 5.0,
            # 'importancia_estudio': importancia

        }
        form = EstudioForm(data=valores)

        self.assertFalse(form.is_valid())

    def test_via_cota_inferior(self):
        """
        VIA inferior bien calculado
        """

        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 0
        v_test.pondExtension = 0
        v_test.pondDuracion = 0
        v_test.pondReversibilidad = 0
        v_test.pondProbabilidad = 0

        via = _calcular_via(v_test, 0, 0, 0, 0, 0)

        self.assertEqual(via, 0.0)

    def test_via_cota_superior(self):
        """
        VIA superior bien calculado
        """

        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 10
        v_test.pondExtension = 10
        v_test.pondDuracion = 10
        v_test.pondReversibilidad = 10
        v_test.pondProbabilidad = 10

        via = _calcular_via(v_test, 10, 10, 10, 10, 10)

        self.assertEqual(via, 5.0)

    def test_no_cambiaron_nivel_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """

        nivel_relevancia_2 = (
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
            )

        self.assertEqual(NIVEL_RELEVANCIA[0][0], nivel_relevancia_2[0][0])
        self.assertEqual(NIVEL_RELEVANCIA[1][0], nivel_relevancia_2[1][0])
        self.assertEqual(NIVEL_RELEVANCIA[2][0], nivel_relevancia_2[2][0])

        self.assertEqual(NIVEL_RELEVANCIA[0][1], nivel_relevancia_2[0][1])
        self.assertEqual(NIVEL_RELEVANCIA[1][1], nivel_relevancia_2[1][1])
        self.assertEqual(NIVEL_RELEVANCIA[2][1], nivel_relevancia_2[2][1])

    def test_no_cambiaron_tipo_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        tipo_relevancia_2 = (
            ('DI', 'Directo'),
            ('IN', 'Indirecto'),
        )
        self.assertEqual(TIPO_RELEVANCIA[0][0], tipo_relevancia_2[0][0])
        self.assertEqual(TIPO_RELEVANCIA[1][0], tipo_relevancia_2[1][0])

        self.assertEqual(TIPO_RELEVANCIA[0][1], tipo_relevancia_2[0][1])
        self.assertEqual(TIPO_RELEVANCIA[1][1], tipo_relevancia_2[1][1])

    def test_no_cambiaron_grado_perturbacion(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        grado_pertubacion_2 = (
            ('F', 'Fuerte'),
            ('M', 'Medio'),
            ('S', 'Suave'),
        )
        self.assertEqual(GRADO_PERTUBACION[0][0], grado_pertubacion_2[0][0])
        self.assertEqual(GRADO_PERTUBACION[1][0], grado_pertubacion_2[1][0])
        self.assertEqual(GRADO_PERTUBACION[2][0], grado_pertubacion_2[2][0])

        self.assertEqual(GRADO_PERTUBACION[0][1], grado_pertubacion_2[0][1])
        self.assertEqual(GRADO_PERTUBACION[1][1], grado_pertubacion_2[1][1])
        self.assertEqual(GRADO_PERTUBACION[2][1], grado_pertubacion_2[2][1])

    def test_http_reponse_ok_tabla(self):
        """
        Estatu Ok HTTP de la pagina de la tabla
        """
        response = self.client.get('/configuracion/index/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_tabla(self):
        """
            Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/index/')
        self.assertTemplateUsed(response, 'configuracion/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_formulario(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_formulario(self):
        """
        Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertTemplateUsed(response, 'configuracion/agregar_estudio.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_tablas(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_tablas(self):
        """
        Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertTemplateUsed(response, 'configuracion/tablas.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_modificar_tablas(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_modificar_tablas(self):
        """
            Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/modificar_tablas/')
        self.assertTemplateUsed(response, 'configuracion/modificar_tablas.html')
        self.assertTemplateUsed(response, 'base.html')


class PruebaFormularioEstudio(SeleniumTestCase):
    """
    Prueba Formulario Estudio
    """
    fixtures = ['users-and-groups.json']


    def test_navegador(self): #pylint: disable=too-many-statements
        """
        test del navegador
        """
        self.selenium.get('{}{}'.format(self.live_server_url, reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        self.selenium.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        nombre = "Impacto F"
        self.selenium.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        select_tipo.select_by_visible_text('Fisico')
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)
        #agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        # Hacemos click en agregar
        self.selenium.find_element_by_name('editar').click()
        #para las alertas del navegador
        confirmacion = self.selenium.switch_to.alert
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        # Hacemos click en agregar
        self.selenium.find_element_by_css_selector('.btn').click()
        nombre = "Impacto B"
        #agregamos el nombre
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        # select_tipo.select_by_visible_text('Biologico')
        #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 720)")
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)

        # agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Socio-Cultural
        self.selenium.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        nombre = "Impacto SC"
        self.selenium.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        # select_tipo.select_by_visible_text('Socio-Cultural')
        #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 720)")
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)
        #agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        # Hacemos click en agregar
        self.selenium.find_element_by_name('editar').click()
        #para las alertas del navegador
        confirmacion = self.selenium.switch_to.alert
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Intentamos agregar un impacto que ya se encuentra registrado
        self.selenium.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        #agregamos el nombre Impacto SC
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        self.selenium.execute_script("window.scrollTo(0, 720)") # movemos el scroll un poco

        # agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)

        # agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)

        # agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)

        # agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)

        # agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)


        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.find_element_by_name('nombre').clear()
        time.sleep(1)

        # agregamos el nombre no repetido
        self.selenium.find_element_by_name('nombre').send_keys('Impacto 5')
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Visualizando los datos del impacto SC y modificandolos
        consulta = Estudio.objects.get(nombre=nombre)
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco
        self.selenium.find_element_by_name('nombre').clear()

        #agregamos el nombre
        self.selenium.find_element_by_name('nombre').send_keys("Este es un nuevo nombre")
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        self.selenium.find_element_by_name('pondExtension').clear()

        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(0)
        self.selenium.find_element_by_name('pondDuracion').clear()

        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(20)
        self.selenium.find_element_by_name('pondReversibilidad').clear()

        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(40)
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Consultando los datos y Eliminando el impacto F cambiado
        nombre = "Impacto F"
        consulta = Estudio.objects.get(nombre=nombre)
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        self.selenium.find_element_by_name('eliminar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        ### Prueba a bases de calculo ###
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/modificar_tablas/'))
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco

        self.selenium.find_element_by_name('valor1').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor1').send_keys("9.0")
        self.selenium.find_element_by_name('valor2').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor2').send_keys("6.0")
        self.selenium.find_element_by_name('valor6').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor6').send_keys("6.0")
        self.selenium.find_element_by_name('valor8').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor8').send_keys("1.0")
        self.selenium.find_element_by_name('valor9').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor9').send_keys("4.0")
        self.selenium.find_element_by_name('valor12').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor12').send_keys("0.0")
        self.selenium.find_element_by_name('valor13').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor13').send_keys("9.0")
        self.selenium.find_element_by_name('valor14').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor14').send_keys("6.0")
        self.selenium.find_element_by_name('valor15').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor15').send_keys("4.0")
        self.selenium.find_element_by_name('valor16').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor16').send_keys("1.0")
        self.selenium.find_element_by_name('valor17').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor17').send_keys("1.0")
        self.selenium.find_element_by_name('valor19').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor19').send_keys("8.0")
        self.selenium.find_element_by_name('valor21').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor21').send_keys("9.0")
        self.selenium.find_element_by_name('valor24').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor24').send_keys("0.0")
        self.selenium.find_element_by_name('valor27').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor27').send_keys("2.0")
        self.selenium.find_element_by_name('valor32').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor32').send_keys("1.0")
        self.selenium.find_element_by_name('submit').click()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/tablas/'))
