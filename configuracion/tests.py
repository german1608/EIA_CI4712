from django.test import LiveServerTestCase, Client
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from configuracion.models import *
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class PruebaFormularioEstudio(StaticLiveServerTestCase):
    port = 8005

    def setUp(self):
        self.client = Client() #Pruebas con testing tools de django
        super(PruebaFormularioEstudio, self).setUp()

    # def test_http_reponse_ok_tabla(self):
    #     # Estatu Ok HTTP de la pagina de la tabla
    #     response = self.client.get('/configuracion/index/')
    #     self.assertEquals(response.status_code, 200)

    # def test_templates_correctos_tabla(self):
    #     # Carga exitosa de los Templates
    #     response = self.client.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
    #     self.assertTemplateUsed(response, 'configuracion/index.html')
    #     self.assertTemplateUsed(response, 'configuracion/base.html')

    # def test_http_reponse_ok_formulario(self):
    #     # Estatu Ok HTTP del formulario
    #     response = self.client.get('/configuracion/agregar_estudio/')
    #     self.assertEquals(response.status_code, 200)

    # def test_templates_correctos_formulario(self):
    #     # Carga exitosa de los Templates
    #     response = self.client.get('%s%s' % (self.live_server_url, '/configuracion/agregar_estudio/'))
    #     self.assertTemplateUsed(response, 'configuracion/agregar_estudio.html')
    #     self.assertTemplateUsed(response, 'configuracion/base.html')

    def test_llenar_formulario(self):
        #Llenamos distintos formularios
        self.client = None
        self.browser = webdriver.Firefox() #Pruebas de navegador con selenium
        self.browser.maximize_window()
        # LLenamos la tabla con datos
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        self.browser.find_element_by_css_selector('.btn.menu').click() # Hacemos click en volver
        time.sleep(3)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en  agregar nuevamente
        time.sleep(4)

        nombre_uno = "Impacto 1"
        self.browser.find_element_by_name('nombre').send_keys(nombre_uno) #agregamos el nombre
        # form_step = self.browser.find_element_by_name('nombre')
        # step = form_step.get_attribute("value")
        # self.assertEqual(step, nombre_uno)

        # time.sleep(2)
        # self.browser.find_element_by_name('clasificacion_probabilidad').send_keys(8) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('pondIntensidad').send_keys(15) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(10) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(30) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(25) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        confirmacion.dismiss()
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(5)
        nombre = "Impacto 2"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        # time.sleep(2)
        # self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
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

        # Agregamos otro elemento pero ahora de tipo Socio-Cultural
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        nombre = "Impacto 3"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Socio-Cultural')
        # time.sleep(2)
        # self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) #agregamos la ponderacion de la duracion
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
        
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Agregamos otro impacto de tipo biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        nombre = "Impacto 4"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        time.sleep(2)
        select_relevancia = Select(self.browser.find_element_by_name('valoracion_relevancia'))
        time.sleep(2)
        select_relevancia.select_by_visible_text('Medio')
        time.sleep(2)
        select_tipo_relevancia = Select(self.browser.find_element_by_name('tipo_relevancia'))
        time.sleep(2)
        select_tipo_relevancia.select_by_visible_text('Indirecto')
        # time.sleep(2)
        # self.browser.find_element_by_name('probabilidad').send_keys(6) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(0) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(0)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(40) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(50) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        #Intentamos agregar un impacto que ya se encuentra registrado
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(3)
        nombre = "Impacto 3"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Fisico')
        # time.sleep(2)
        # self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
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
        time.sleep(5)

        #Visualizando los datos del impacto 1 y modificandolos
        consulta = Estudio.objects.get(nombre=nombre_uno)
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
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        #Consultando los datos cambiados y Eliminando el impacto 1 cambiado
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(7)
        self.browser.find_element_by_name('eliminar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        # Prueba de ponderaciones
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        nombre = "Impacto 6"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        # time.sleep(2)
        # self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(21) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)  #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        ### Prueba a bases de calculo ###
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/tablas/'))
        time.sleep(4)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_css_selector('.btn').click()
        time.sleep(4)
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


        # Prueba para las validaciones
        # self.browser.find_element_by_css_selector('.btn').click()
        # time.sleep(2)
        # self.browser.find_element_by_name('valor32').clear()
        # confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        # time.sleep(2)
        # confirmacion.accept()


    def tearDown(self):
        # Llama al tearDown al cerrar el browser
        self.browser.quit()
        super(PruebaFormularioEstudio, self).tearDown()


