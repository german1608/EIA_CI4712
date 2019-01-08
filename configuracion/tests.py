"""
Pruebas Unitarias
"""
# pylint: disable=too-many-lines
import time
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from selenium.webdriver.support.ui import Select
from configuracion.models import NIVEL_RELEVANCIA, TIPO_RELEVANCIA, GRADO_PERTUBACION
from configuracion.models import VALOR_SA, EXT_CLASIFICACION, DUR_CRITERIOS, REV_CLASIFICACION
from configuracion.models import NIVEL_IMPORTANCIA, PROBABILIDAD, MEDIOS
from configuracion.views import _calcular_via
from configuracion.forms import EstudioForm
from configuracion.models import Intensidad, Probabilidad, Extension, Reversibilidad
from configuracion.models import Duracion, Importancia, Estudio, Macro, Disciplina
from configuracion.models import Actividad, Plan
from utils.testutils import SeleniumTestCase

class KaraotaTests(TestCase): # pylint: disable=too-many-public-methods
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

    def test_database_estudio(self): # pylint: disable=no-self-use
        """
        aaaa
        """
        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 0
        v_test.pondExtension = 0
        v_test.pondDuracion = 0
        v_test.pondReversibilidad = 0
        v_test.pondProbabilidad = 0

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
        self.assertEqual(NIVEL_RELEVANCIA, (
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
            ))

    def test_no_cambiaron_tipo_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        self.assertEqual(TIPO_RELEVANCIA, (
            ('DI', 'Directo'),
            ('IN', 'Indirecto'),
        ))

    def test_no_cambiaron_grado_perturbacion(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        self.assertEqual(GRADO_PERTUBACION, (
            ('F', 'Fuerte'),
            ('M', 'Medio'),
            ('S', 'Suave'),
        ))

    def test_no_cambiaron_valor_sa(self):
        """
            se verifica que nadie cambio los valores_sa
        """
        self.assertEqual(VALOR_SA, (
            ('MA', 'Muy Alto'),
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
        ))

    def test_no_cambiaron_ext_clasificacion(self):
        """
            se verifica que nadie cambio ext_clasificacion
        """
        self.assertEqual(EXT_CLASIFICACION, (
            ('GE', 'Generalizada (>75%)'),
            ('EX', 'Extensiva (35-74%)'),
            ('LO', 'Local (10-34%)'),
            ('PU', 'Puntual (<10%)'),
            ))

    def test_no_cambiaron_dur_criterios(self):
        """
            se verifica que nadie cambio dur_clasifiacion
        """
        self.assertEqual(DUR_CRITERIOS, (
            ('M2', 'Menos de 2 años'),
            ('M2-5', '2 a 5 años'),
            ('M5-10', '5 a 10 años'),
            ('M10', 'Mas de 10 años'),
            ))

    def test_no_cambiaron_rev_clasificacion(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        self.assertEqual(REV_CLASIFICACION, (
            ('IR', 'Irreversible'),
            ('TR', 'Requiere Tratamiento'),
            ('MR', 'Medianamente Reversible'),
            ('RE', 'Reversible'),
            ))

    def test_no_cambiaron_probabilidad(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        self.assertEqual(PROBABILIDAD, (
            ('A', 'Alta'),
            ('M', 'Media'),
            ('B', 'Baja'),
            ('N', 'Nula'),
            ))

    def test_no_cambiaron_nivel_importancia(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        self.assertEqual(NIVEL_IMPORTANCIA, (
            ('MA', 'Muy Alta'),
            ('A', 'Alta'),
            ('M', 'Media'),
            ('B', 'Baja'),
            ))

    def test_no_cambiaron_medios(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        self.assertEqual(MEDIOS, (
            ('FS', 'Fisico'),
            ('BIO', 'Biologico'),
            ('SC', 'Socio-Cultural'),
            ))

    def test_http_reponse_ok_tabla(self):
        """
        Estatus Ok HTTP de la pagina de la tabla
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

class TestsIntegridadDatosTablasEstudio(TestCase): # pylint: disable=too-many-public-methods
    '''
        Test de las bases de calculo
    '''
    def setUp(self):
        '''
        Se crean instancias para las pruebas
        '''
        #Intensidad
        self.intensidad = [[None, None, None],
                           [None, None, None],
                           [None, None, None],
                           [None, None, None]]

        self.intensidad[0][0] = Intensidad.objects.filter(
            valor_sociocultural="MA",
            grado_perturbacion="F").first()
        self.intensidad[0][1] = Intensidad.objects.filter(
            valor_sociocultural="MA",
            grado_perturbacion="M").first()
        self.intensidad[0][2] = Intensidad.objects.filter(
            valor_sociocultural="MA",
            grado_perturbacion="S").first()
        self.intensidad[1][0] = Intensidad.objects.filter(
            valor_sociocultural="A",
            grado_perturbacion="F").first()

        self.intensidad[1][1] = Intensidad.objects.filter(
            valor_sociocultural="A",
            grado_perturbacion="M").first()
        self.intensidad[1][2] = Intensidad.objects.filter(
            valor_sociocultural="A",
            grado_perturbacion="S").first()

        self.intensidad[2][0] = Intensidad.objects.filter(
            valor_sociocultural="M",
            grado_perturbacion="F").first()
        self.intensidad[2][1] = Intensidad.objects.filter(
            valor_sociocultural="M",
            grado_perturbacion="M").first()
        self.intensidad[2][2] = Intensidad.objects.filter(
            valor_sociocultural="M",
            grado_perturbacion="S").first()

        self.intensidad[3][0] = Intensidad.objects.filter(
            valor_sociocultural="B",
            grado_perturbacion="F").first()
        self.intensidad[3][1] = Intensidad.objects.filter(
            valor_sociocultural="B",
            grado_perturbacion="M").first()
        self.intensidad[3][2] = Intensidad.objects.filter(
            valor_sociocultural="B",
            grado_perturbacion="S").first()

        #Extension
        self.extension = [None, None, None, None]
        self.extension[0] = Extension.objects.filter(clasificacion="GE").first()
        self.extension[1] = Extension.objects.filter(clasificacion="EX").first()
        self.extension[2] = Extension.objects.filter(clasificacion="LO").first()
        self.extension[3] = Extension.objects.filter(clasificacion="PU").first()


        #Duracion
        self.duracion = [None, None, None, None]

        self.duracion[0] = Duracion.objects.filter(criterio="M10").first()
        self.duracion[1] = Duracion.objects.filter(criterio="M5-10").first()
        self.duracion[2] = Duracion.objects.filter(criterio="M2-5").first()
        self.duracion[3] = Duracion.objects.filter(criterio="M2").first()

        #Reversibilidad
        self.reversibilidad = [None, None, None, None]
        self.reversibilidad[0] = Reversibilidad.objects.filter(clasificacion="IR").first()
        self.reversibilidad[1] = Reversibilidad.objects.filter(clasificacion="TR").first()
        self.reversibilidad[2] = Reversibilidad.objects.filter(clasificacion="MR").first()
        self.reversibilidad[3] = Reversibilidad.objects.filter(clasificacion="RE").first()

        #Importancia
        self.importancia = [None, None, None, None]
        self.importancia[0] = Importancia.objects.filter(importancia="MA").first()
        self.importancia[1] = Importancia.objects.filter(importancia="A").first()
        self.importancia[2] = Importancia.objects.filter(importancia="M").first()
        self.importancia[3] = Importancia.objects.filter(importancia="B").first()

        #Probabilidad

        self.probabilidad = [None, None, None, None]
        self.probabilidad[0] = Probabilidad.objects.filter(probabilidad="A").first()
        self.probabilidad[1] = Probabilidad.objects.filter(probabilidad="M").first()
        self.probabilidad[2] = Probabilidad.objects.filter(probabilidad="B").first()
        self.probabilidad[3] = Probabilidad.objects.filter(probabilidad="N").first()

    def test_intensidad_transitividad_ma(self):
        """
            aa
        """
        self.assertTrue((self.intensidad[0][0].valor >= self.intensidad[0][1].valor) and
                        (self.intensidad[0][1].valor >= self.intensidad[0][2].valor))

    def test_intensidad_limites_ma(self):
        """
            aa
        """
        self.assertTrue(self.intensidad[1][0].valor >= 0 and self.intensidad[1][2].valor <= 10)

    def test_intensidad_transitividad_a(self):
        """
            aa
        """
        self.assertTrue((self.intensidad[1][0].valor >= self.intensidad[1][1].valor) and
                        (self.intensidad[1][1].valor >= self.intensidad[1][2].valor))

    def test_intensidad_limites_a(self):
        """
            aa
        """
        self.assertTrue(self.intensidad[1][0].valor >= 0 and self.intensidad[1][2].valor <= 10)

    def test_intensidad_transitividad_m(self):
        """
        aaaa
        """
        self.assertTrue((self.intensidad[2][0].valor >= self.intensidad[2][1].valor) and
                        (self.intensidad[2][1].valor >= self.intensidad[2][2].valor))

    def test_intensidad_limites_m(self):
        """
            aa
        """
        self.assertTrue(self.intensidad[2][0].valor >= 0 and self.intensidad[2][2].valor <= 10)

    def test_intensidad_transitividad_b(self):
        """
            aa
        """
        self.assertTrue((self.intensidad[3][0].valor >= self.intensidad[3][1].valor) and
                        (self.intensidad[3][1].valor >= self.intensidad[3][2].valor))

    def test_intensidad_limites_b(self):
        """
            aa
        """
        self.assertTrue(self.intensidad[3][0].valor >= 0 and self.intensidad[3][2].valor <= 10)

    def test_extension_transitividad(self):
        """
            aa
        """
        self.assertTrue((self.extension[0].valor >= self.extension[1].valor) and
                        (self.extension[1].valor >= self.extension[2].valor) and
                        (self.extension[2].valor >= self.extension[3].valor))

    def test_extension_limites(self):
        """
            aa
        """
        self.assertTrue(self.extension[0].valor >= 0 and self.extension[3].valor <= 10)

    def test_duracion_transitividad(self):
        """
            aa
        """
        self.assertTrue((self.duracion[0].valor >= self.duracion[1].valor) and
                        (self.duracion[1].valor >= self.duracion[2].valor) and
                        (self.duracion[2].valor >= self.duracion[3].valor))

    def test_duracion_limites(self):
        """
            aa
        """
        self.assertTrue(self.duracion[0].valor >= 0 and self.duracion[3].valor <= 10)

    def test_reversibilidad_transitividad(self):
        """
            aa
        """
        self.assertTrue((self.reversibilidad[0].valor >= self.reversibilidad[1].valor) and
                        (self.reversibilidad[1].valor >= self.reversibilidad[2].valor) and
                        (self.reversibilidad[2].valor >= self.reversibilidad[3].valor))

    def test_reversibilidad_limites(self):
        """
            aa
        """
        self.assertTrue(self.reversibilidad[0].valor >= 0 and self.reversibilidad[3].valor <= 10)

    def test_importancia_transitividad(self):
        """
            aa
        """
        self.assertTrue((self.importancia[0].valor >= self.importancia[1].valor) and
                        (self.importancia[1].valor >= self.importancia[2].valor) and
                        (self.importancia[2].valor >= self.importancia[3].valor))

    def test_importancia_limites(self):
        """
            aa
        """
        self.assertTrue(self.importancia[0].valor >= 0 and self.importancia[3].valor <= 10)

    def test_probabilidad_transitividad(self):
        """
            aa
        """
        self.assertTrue((self.probabilidad[0].valor >= self.probabilidad[1].valor) and
                        (self.probabilidad[1].valor >= self.probabilidad[2].valor) and
                        (self.probabilidad[2].valor >= self.probabilidad[3].valor))

    def test_probabilidad_limites(self):
        """
            aa
        """
        self.assertTrue(self.probabilidad[0].valor >= 0 and self.probabilidad[3].valor <= 100)


    def test_insertar_macro(self):
        """
        aa
        """
        mac = Macro.objects.create(
            nombre="test_macro",
            descripcion="test_descripcion",
            proyecto="test_proyecto")

        mac2 = Macro.objects.filter(nombre="test_macro").first()

        self.assertEqual(mac.id, mac2.id)

    def test_insertar_disciplina(self):
        """
        aa
        """
        dis = Disciplina.objects.create(
            nombre="test_disciplina",
            descripcion="test_descripcion",
            proyecto="test_proyecto")
        dis2 = Disciplina.objects.filter(nombre="test_disciplina").first()
        self.assertEqual(dis.id, dis2.id)

    def test_insertar_actividad(self):
        """
        aa
        """
        mac = Macro.objects.create( #pylint: disable=unused-variable
            nombre="test_macro",
            descripcion="test_descripcion",
            proyecto="test_proyecto")
        mac2 = Macro.objects.filter(nombre="test_macro").first()
        dis = Disciplina.objects.create( #pylint: disable=unused-variable
            nombre="test_disciplina",
            descripcion="test_descripcion",
            proyecto="test_proyecto")
        dis2 = Disciplina.objects.filter(nombre="test_disciplina").first()
        act = Actividad.objects.create(
            nombre="test_actividad",
            descripcion="test_descripcion",
            disciplina=dis2,
            macro=mac2,
            amenazas="Test amenaza")
        act2 = Actividad.objects.filter(nombre="test_actividad").first()
        self.assertEqual(act.id, act2.id)

    def test_insertar_estudio(self):
        """
            aa
        """
        intensidad2 = Intensidad.objects.filter(
            valor_sociocultural="MA",
            grado_perturbacion="F").first()
        extension2 = Extension.objects.filter(
            clasificacion="GE").first()
        duracion2 = Duracion.objects.filter(
            criterio="M10").first()
        reversibilidad2 = Reversibilidad.objects.filter(
            clasificacion="IR").first()
        importancia2 = Importancia.objects.filter(
            importancia="MA").first()
        probabilidad2 = Probabilidad.objects.filter(
            probabilidad="A").first()

        est = Estudio.objects.create(
            nombre="test_estudio",
            tipo="FS",
            valoracion_relevancia="MA",
            tipo_relevancia="DI",
            intensidad=intensidad2,
            extension=extension2,
            duracion=duracion2,
            reversibilidad=reversibilidad2,
            probabilidad=probabilidad2,
            pondIntensidad="20",
            pondExtension="20",
            pondDuracion="20",
            pondReversibilidad="20",
            pondProbabilidad="20",
            via="5",
            importancia_estudio=importancia2
        )

        est2 = Estudio.objects.filter(nombre="test_estudio").first()

        self.assertEqual(est.id, est2.id)

    def test_insertar_plan(self):
        """
        aa
        """
        plan = Plan.objects.create(
            nombre="Test plan",
            medidas="Test medidas",
            objetivo_general="Objetivo general test",
            objetivo_especifico="Objetivo especficio test",
            alcance="alto",
            metodologia="metodologia",
            cronograma="crono",
            responsable="responsable",
            costo=1,
            proyecto="p2"
        )

        plan2 = Plan.objects.filter(nombre="Test plan").first()
        self.assertEqual(plan.id, plan2.id)

    def test_insertar_mal_plan(self):
        """
        aa
        """
        plan = "" #pylint: disable=possibly-unused-variable
        se_creo = False
        try:
            plan = Plan.objects.create(
                nombre="Test plan_2",
                medidas="Test medidas",
                objetivo_general="Objetivo general test",
                objetivo_especifico="Objetivo especficio test",
                alcance="alto",
                metodologia="metodologia",
                cronograma="crono",
                responsable="responsable",
                costo="wadawd",
                proyecto="p2"
            )
            se_creo = True
        except ValueError:
            #print("falla: "+str(plan))
            #Deberia fallar porque el costo no es un flotante
            se_creo = False

        if not "plan" in locals():
            se_creo = False
        self.assertFalse(se_creo)
