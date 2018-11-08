from django.test import Client
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from configuracion.models import *
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from django.test import TestCase
from configuracion.models import NIVEL_RELEVANCIA, TIPO_RELEVANCIA, GRADO_PERTUBACION
from configuracion.views import _calcular_via, EstudioCreate
from configuracion.forms import EstudioForm

class KaraotaTests(TestCase):

    def setUp(self):
        self.client = Client() #Pruebas con testing tools de django

    def tearDown(self):
        self.client=None

    def test_ponderaciones_iguala101(self):
        valores={
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

        via = _calcular_via(v_test, 0, 0, 0,0,0)

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

        via = _calcular_via(v_test, 10, 10, 10,10, 10)

        self.assertEqual(via, 5.0)      

    def test_no_cambiaron_nivel_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """

        NIVEL_RELEVANCIA2 = (
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
            )
        
        self.assertEqual(NIVEL_RELEVANCIA[0][0], NIVEL_RELEVANCIA2[0][0])       
        self.assertEqual(NIVEL_RELEVANCIA[1][0], NIVEL_RELEVANCIA2[1][0])   
        self.assertEqual(NIVEL_RELEVANCIA[2][0], NIVEL_RELEVANCIA2[2][0])       

        self.assertEqual(NIVEL_RELEVANCIA[0][1], NIVEL_RELEVANCIA2[0][1])       
        self.assertEqual(NIVEL_RELEVANCIA[1][1], NIVEL_RELEVANCIA2[1][1])   
        self.assertEqual(NIVEL_RELEVANCIA[2][1], NIVEL_RELEVANCIA2[2][1])   

    def test_no_cambiaron_tipo_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        TIPO_RELEVANCIA2 = (
            ('DI', 'Directo'),
            ('IN', 'Indirecto'),
        )
        self.assertEqual(TIPO_RELEVANCIA[0][0], TIPO_RELEVANCIA2[0][0])     
        self.assertEqual(TIPO_RELEVANCIA[1][0], TIPO_RELEVANCIA2[1][0]) 

        self.assertEqual(TIPO_RELEVANCIA[0][1], TIPO_RELEVANCIA2[0][1])     
        self.assertEqual(TIPO_RELEVANCIA[1][1], TIPO_RELEVANCIA2[1][1]) 

    def test_no_cambiaron_grado_perturbacion(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        GRADO_PERTUBACION2 = (
            ('F', 'Fuerte'),
            ('M', 'Medio'),
            ('S', 'Suave'),
        )
        self.assertEqual(GRADO_PERTUBACION[0][0], GRADO_PERTUBACION2[0][0])     
        self.assertEqual(GRADO_PERTUBACION[1][0], GRADO_PERTUBACION2[1][0]) 
        self.assertEqual(GRADO_PERTUBACION[2][0], GRADO_PERTUBACION2[2][0]) 
        
        self.assertEqual(GRADO_PERTUBACION[0][1], GRADO_PERTUBACION2[0][1])     
        self.assertEqual(GRADO_PERTUBACION[1][1], GRADO_PERTUBACION2[1][1]) 
        self.assertEqual(GRADO_PERTUBACION[2][1], GRADO_PERTUBACION2[2][1])

    def test_http_reponse_ok_tabla(self):
        # Estatu Ok HTTP de la pagina de la tabla
        response = self.client.get('/configuracion/index/')
        self.assertEquals(response.status_code, 200)

    def test_templates_correctos_tabla(self):
        # Carga exitosa de los Templates
        response = self.client.get('/configuracion/index/')
        self.assertTemplateUsed(response, 'configuracion/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_formulario(self):
        # Estatu Ok HTTP del formulario
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertEquals(response.status_code, 200)

    def test_templates_correctos_formulario(self):
        # Carga exitosa de los Templates
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertTemplateUsed(response, 'configuracion/agregar_estudio.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_tablas(self):
        # Estatu Ok HTTP del formulario
        response = self.client.get('/configuracion/tablas/')
        self.assertEquals(response.status_code, 200)

    def test_templates_correctos_tablas(self):
        # Carga exitosa de los Templates
        response = self.client.get('/configuracion/tablas/')
        self.assertTemplateUsed(response, 'configuracion/tablas.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_modificar_tablas(self):
        # Estatu Ok HTTP del formulario
        response = self.client.get('/configuracion/tablas/')
        self.assertEquals(response.status_code, 200)

    def test_templates_correctos_modificar_tablas(self):
        # Carga exitosa de los Templates
        response = self.client.get('/configuracion/modificar_tablas/')
        self.assertTemplateUsed(response, 'configuracion/modificar_tablas.html')
        self.assertTemplateUsed(response, 'base.html')
        

class PruebaFormularioEstudio(StaticLiveServerTestCase):
    port = 8005

    def setUp(self):
        
        super(PruebaFormularioEstudio, self).setUp()
        #Llenamos distintos formularios
        self.browser = webdriver.Firefox() #Pruebas de navegador con selenium
        self.browser.maximize_window()

    def test_navegador(self):

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(5)
        nombre = "Impacto F"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Fisico')
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        #agregamos la ponderacion de la intensidad
        self.browser.find_element_by_name('pondIntensidad').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la extension
        self.browser.find_element_by_name('pondExtension').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la duracion
        self.browser.find_element_by_name('pondDuracion').send_keys(30)
        time.sleep(2)
        #agregamos la ponderacion de la reversibilidad
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        #agregamos la ponderacion de la probabilidad
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)
        time.sleep(2)
        # Hacemos click en agregar
        self.browser.find_element_by_name('editar').click()
        time.sleep(2)
        #para las alertas del navegador
        confirmacion = self.browser.switch_to.alert 
        time.sleep(2)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        # Hacemos click en agregar
        self.browser.find_element_by_css_selector('.btn').click()
        time.sleep(5)
        nombre = "Impacto B"
        #agregamos el nombre
        self.browser.find_element_by_name('nombre').send_keys(nombre)
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        time.sleep(2)
        #movemos el scroll un poco
        self.browser.execute_script("window.scrollTo(0, 720)")
        time.sleep(2)
        #agregamos la ponderacion de la intensidad
        self.browser.find_element_by_name('pondIntensidad').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la extension
        self.browser.find_element_by_name('pondExtension').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la duracion
        self.browser.find_element_by_name('pondDuracion').send_keys(30)
        time.sleep(2)
        #agregamos la ponderacion de la reversibilidad
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)  #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)
        
        # Volvemos a agregar otro elemento pero ahora de tipo Socio-Cultural
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(5)
        nombre = "Impacto SC"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Socio-Cultural')
        time.sleep(2)
        #movemos el scroll un poco
        self.browser.execute_script("window.scrollTo(0, 720)")
        time.sleep(2)
        #agregamos la ponderacion de la intensidad
        self.browser.find_element_by_name('pondIntensidad').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la extension
        self.browser.find_element_by_name('pondExtension').send_keys(20)
        time.sleep(2)
        #agregamos la ponderacion de la duracion
        self.browser.find_element_by_name('pondDuracion').send_keys(30)
        time.sleep(2)
        #agregamos la ponderacion de la reversibilidad
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        #agregamos la ponderacion de la probabilidad
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)
        time.sleep(2)
        # Hacemos click en agregar
        self.browser.find_element_by_name('editar').click()
        time.sleep(2)
        #para las alertas del navegador
        confirmacion = self.browser.switch_to.alert
        time.sleep(2)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)
        
        #Intentamos agregar un impacto que ya se encuentra registrado
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(3)
        #agregamos el nombre Impacto SC
        self.browser.find_element_by_name('nombre').send_keys(nombre)
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30)  #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        time.sleep(4)
        self.browser.find_element_by_name('nombre').clear()
        time.sleep(2)
        self.browser.find_element_by_name('nombre').send_keys('Impacto 5') #agregamos el nombre no repetido
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)
        
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        #Visualizando los datos del impacto SC y modificandolos
        consulta = Estudio.objects.get(nombre=nombre)
        time.sleep(2)
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(10)
        self.browser.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('nombre').clear()
        time.sleep(2)
        self.browser.find_element_by_name('nombre').send_keys("Este es un nuevo nombre") #agregamos el nombre
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(5)
        self.browser.find_element_by_name('pondExtension').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(0) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(20)  #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(40) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(10)
        self.browser.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco
        time.sleep(2)
        
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        #Consultando los datos y Eliminando el impacto F cambiado
        nombre="Impacto F"
        consulta = Estudio.objects.get(nombre=nombre)
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('eliminar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        ### Prueba a bases de calculo ###
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/modificar_tablas/'))
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(2)

        self.browser.find_element_by_name('valor1').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor1').send_keys("9.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor2').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor2').send_keys("6.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor6').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor6').send_keys("6.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor8').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor8').send_keys("1.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor9').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor9').send_keys("4.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor12').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor12').send_keys("0.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor13').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor13').send_keys("9.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor14').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor14').send_keys("6.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor15').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor15').send_keys("4.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor16').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor16').send_keys("1.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor17').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor17').send_keys("1.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor19').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor19').send_keys("8.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor21').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor21').send_keys("9.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor24').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor24').send_keys("0.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor27').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor27').send_keys("2.0")
        time.sleep(1)
        self.browser.find_element_by_name('valor32').clear()
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        #self.browser.find_element_by_name('valor32').send_keys("1.0")
        time.sleep(2)
        self.browser.find_element_by_name('submit').click()
        time.sleep(5)
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/tablas/'))
        time.sleep(4)

    def tearDown(self):
        # Llama al tearDown al cerrar el browser
        self.browser.quit()
        super(PruebaFormularioEstudio, self).tearDown()


