"""
    Archivo para las pruebas realizadas en selenium
"""
import os
from django.urls import reverse
from utils.testutils import SeleniumTestCase
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import



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
            tipo="prueba selenium")
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


class TestOrganizaciones(SeleniumTestCase):
    """
        Clase para probar las organizaciones del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium")

        self.organizacion = Organizacion.objects.create(
            proyecto=self.proyecto,
            razon_social="natural",
            nombre="Nombre",
            direccion="Direccion",
            rif="V-25872052-5",
            nombre_representante_legal="NombreR",
            apellido_representante_legal="Apellido",
            cedula_representante_legal="V25991612",
            pasaporte_representante_legal=25872061,
            telefono="04141234567",
            email="prueba@gmail.ve")

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_organizacion(self):
        """
            Test para anadir datos de una organizacion.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector(
            '#datos-organizaciones').click()
        self.selenium.find_element_by_css_selector('#add').click()
        proy = self.proyecto.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        razon_social = "natural"
        self.selenium.find_element_by_name(
            'razon_social').send_keys(razon_social)
        nombre = "Nombre"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        rif = "V-25972062-4"
        self.selenium.find_element_by_name('rif').send_keys(rif)
        direccion = "Direccion"
        self.selenium.find_element_by_name('direccion').send_keys(direccion)
        representante = "Representante"
        self.selenium.find_element_by_name(
            'nombre_representante_legal').send_keys(representante)
        apellido_representante = "ApellidoRepresentante"
        self.selenium.find_element_by_name(
            'apellido_representante_legal').send_keys(apellido_representante)
        cedula_representante = "V25872062"
        self.selenium.find_element_by_name(
            'cedula_representante_legal').send_keys(cedula_representante)
        pasaporte = 25872061
        self.selenium.find_element_by_name(
            'pasaporte_representante_legal').send_keys(pasaporte)
        telefono = "04141633960"
        self.selenium.find_element_by_name('telefono').send_keys(telefono)
        email = "prueba@gmail.ve"
        self.selenium.find_element_by_name('email').send_keys(email)

    def test_ver_detalles_organizacion(self):
        """
            Probar el boton de ver detalles de una organizacion.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/organizaciones/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.organizacion.id)).click()

    def test_editar_organizacion(self):
        """
            Editar los datos de una organizacion
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/organizaciones/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.organizacion.id)).click()
        nombre = "Edicion de prueba"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_organizacion(self):
        """
            Borrar los datos de una organizacion
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/organizaciones/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.organizacion.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()


class TestResponsable(SeleniumTestCase):
    """
        Clase para probar los responsables del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium")

        # Se crea un responsable para editar y eliminar
        self.responsable = Responsable.objects.create(
            proyecto=self.proyecto,
            nombre="Nombre",
            apellido="Apellido",
            cedula="V25991612",
            pasaporte=25872061,
            nivel_academico="Licenciado",
            tipo_responsable="EsIA")

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_responsable(self):
        """
            Test para anadir datos de un responsable.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector('#responsables').click()
        self.selenium.find_element_by_css_selector('#add').click()
        proy = self.proyecto.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        nombre = "Nombre1"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        apellido = "Apellido1"
        self.selenium.find_element_by_name('apellido').send_keys(apellido)
        cedula = "V25991602"
        self.selenium.find_element_by_name('cedula').send_keys(cedula)
        pasaporte = 25872062
        self.selenium.find_element_by_name('pasaporte').send_keys(pasaporte)
        nivel_academico = "Licenciado"
        self.selenium.find_element_by_name(
            'nivel_academico').send_keys(nivel_academico)
        tipo_responsable = "EsIA"
        self.selenium.find_element_by_name(
            'tipo_responsable').send_keys(tipo_responsable)

    def test_ver_detalles_responsable(self):
        """
            Probar el boton de ver detalles de un responsable.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/responsables/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.responsable.id)).click()

    def test_editar_responsable(self):
        """
            Editar los datos de un responsable
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/responsables/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.responsable.id)).click()
        nombre = "Edicion de prueba"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_responsable(self):
        """
            Borrar los datos de un responsable
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/responsables/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.responsable.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()


class TestDatosDocumento(SeleniumTestCase):
    """
        Clase para probar los datos de documentos del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium")

        # Se crea un documento para editar y eliminar
        self.documento = DatosDocumento.objects.create(
            proyecto=self.proyecto,
            fecha="2007-10-25",
            ciudad="Ciudad",
            estado="Estado",
            pais="Pais")

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_datos_documento(self):
        """
            Test para anadir datos de un documento.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector('#datos-documentos').click()
        self.selenium.find_element_by_css_selector('#add').click()
        proy = self.proyecto.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        fecha = "2007-10-25"
        self.selenium.find_element_by_name('fecha').send_keys(fecha)
        ciudad = "Ciudad"
        self.selenium.find_element_by_name('ciudad').send_keys(ciudad)
        estado = "Estado"
        self.selenium.find_element_by_name('estado').send_keys(estado)
        pais = "Pais"
        self.selenium.find_element_by_name('pais').send_keys(pais)

    def test_ver_detalles_datos_documento(self):
        """
            Probar el boton de ver detalles de un los datos de un documento.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_documentos/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.documento.id)).click()

    def test_editar_datos_documento(self):
        """
            Editar los datos de un documento
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_documentos/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.documento.id)).click()
        ciudad = "Edicion de prueba"
        self.selenium.find_element_by_name('ciudad').send_keys(ciudad)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_datos_documento(self):
        """
            Borrar los datos de un documento
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/datos_documentos/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.documento.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()


class TestSolicitante(SeleniumTestCase):
    """
        Clase para probar los solicitantes del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium",
            )

        # Se crea un solicitante para editar y eliminar
        self.solicitante = Solicitante.objects.create(
            proyecto=self.proyecto,
            nombre="Nombre",
            apellido="Apellido",
            cedula="V25991612",
            pasaporte=25872061,
            telefono="04241234567",
            email="email@gmail.com")

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_solicitante(self):
        """
            Test para anadir datos de un solicitante.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector('#solicitantes').click()
        self.selenium.find_element_by_css_selector('#add').click()
        proy = self.proyecto.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        nombre = "Nombre1"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        apellido = "Apellido1"
        self.selenium.find_element_by_name('apellido').send_keys(apellido)
        cedula = "V25991602"
        self.selenium.find_element_by_name('cedula').send_keys(cedula)
        pasaporte = 25872062
        self.selenium.find_element_by_name('pasaporte').send_keys(pasaporte)
        telefono = "04241234567"
        self.selenium.find_element_by_name('telefono').send_keys(telefono)
        email = "email@gmail.com"
        self.selenium.find_element_by_name('email').send_keys(email)

    def test_ver_detalles_solicitante(self):
        """
            Probar el boton de ver detalles de un solicitante.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/solicitantes/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.solicitante.id)).click()

    def test_editar_solicitante(self):
        """
            Editar los datos de un solicitante
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/solicitantes/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.solicitante.id)).click()
        nombre = "Edicion de prueba"
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_solicitante(self):
        """
            Borrar los datos de un solicitante
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/solicitantes/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.solicitante.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()


class TestDescripcionProyecto(SeleniumTestCase):
    """
        Clase para probar las descripciones de proyectos del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_path = os.path.join(self.base_dir, 'static', 'img', 'germanbb.jpg')
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium",
            )

        self.proyecto1 = DatosProyecto.objects.create(
            titulo="prueba de detalles1",
            ubicacion="caracas, venezuela1",
            area="area de prueba, caracas1",
            tipo="prueba selenium1")

        # Se crea una descripcion de un proyecto para editar y eliminar
        self.descripcion = DescripcionProyecto.objects.create(
            proyecto=self.proyecto,
            obj_general="Obj General",
            obj_especifico="Obj Especifico",
            justificacion="Justificacion",
            area=self.image_path)

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_descripcion(self):
        """
            Test para anadir descripcion de un proyecto.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector(
            '#detalles-proyecto').click()
        self.selenium.find_element_by_css_selector('#add').click()
        proy = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        obj_general = "Obj General"
        self.selenium.find_element_by_name(
            'obj_general').send_keys(obj_general)
        obj_especifico = "Obj Especifico"
        self.selenium.find_element_by_name(
            'obj_especifico').send_keys(obj_especifico)
        justificacion = "Justificacion"
        self.selenium.find_element_by_name(
            'justificacion').send_keys(justificacion)
        area = self.image_path
        self.selenium.find_element_by_name('area').send_keys(area)

    def test_ver_detalles_descripcion(self):
        """
            Probar el boton de ver detalles de una descripcion de un proyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/descripcion_proyecto/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.descripcion.id)).click()

    def test_editar_descripcion(self):
        """
            Editar los datos de una descripcion de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/descripcion_proyecto/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.descripcion.id)).click()
        obj_general = "Edicion de prueba"
        self.selenium.find_element_by_name(
            'obj_general').send_keys(obj_general)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_descripcion(self):
        """
            Borrar los datos de una descripcion de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/descripcion_proyecto/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.descripcion.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()


class TestCaracteristicaMedio(SeleniumTestCase):
    """
        Clase para probar las caracteristicas de los medios del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_path = os.path.join(self.base_dir, 'static', 'img', 'germanbb.jpg')
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium",
            )

        self.proyecto1 = DatosProyecto.objects.create(
            titulo="prueba de detalles1",
            ubicacion="caracas, venezuela1",
            area="area de prueba, caracas1",
            tipo="prueba selenium1")

        self.medio1 = Medio.objects.create(
            tipo="biologico",
            proyecto=self.proyecto1,
            descripcion="descripcion del medio",
            conclusiones="conclusiones sobre el medio"
        )

        self.caracteristica1 = CaracteristicaMedio.objects.create(
            caracteristica="caracteristica",
            medio=self.medio1,
            descripcion="descripcion"
        )

        self.subcaracteristica1 = SubaracteristicaMedio.objects.create(
            nombre_sub='nombre',
            caracteristica=self.caracteristica1,
            atributo='atributo',
            comentario='comentario'
        )

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_medio(self):
        """
            Test para anadir medio de un proyecto.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/'))
        self.selenium.find_element_by_css_selector(
            '#caracteristicas-medio').click()
        self.selenium.find_element_by_css_selector('#add').click()
        tipo = "biologico"
        self.selenium.find_element_by_name(
            'tipo').send_keys(tipo)
        proy = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proy)
        descripcion = "Descripcion del medio"
        self.selenium.find_element_by_name(
            'descripcion').send_keys(descripcion)
        conclusiones= "Conclusiones sobre el medio"
        self.selenium.find_element_by_name(
            'conclusiones').send_keys(conclusiones)

    def test_ver_detalles_medio(self):
        """
            Probar el boton de ver detalles de un medio de un proyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristicas_medio/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.medio1.id)).click()

    def test_editar_medio(self):
        """
            Editar los datos de un medio
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristicas_medio/'))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.medio1.id)).click()
        descripcion = "Edicion de prueba"
        self.selenium.find_element_by_name('descripcion').send_keys(descripcion)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_medio(self):
        """
            Borrar los datos de un medio de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristicas_medio/'))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.medio1.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_anadir_caracteristica(self):
        """
            Test para anadir caracteristica de medio de un proyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristicas_medio/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.medio1.id)).click()
        self.selenium.find_element_by_css_selector('#add').click()
        caracteristica = "caracteristica"
        self.selenium.find_element_by_name(
            'caracteristica').send_keys(caracteristica)
        descripcion = "Descripcion"
        self.selenium.find_element_by_name(
            'descripcion').send_keys(descripcion)

    def test_ver_detalles_caracteristica(self):
        """
            Probar el boton de ver detalles de una caracteristica de medio de un proyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristica_medio/'+str(self.medio1.id) +'/'))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.caracteristica1.id)).click()

    def test_editar_caracteristica(self):
        """
            Editar las caracteristicas de un medio
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristica_medio/'+str(self.medio1.id) +'/' ))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.caracteristica1.id)).click()
        descripcion = "Edicion de prueba"
        self.selenium.find_element_by_name('descripcion').send_keys(descripcion)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_caracteristica(self):
        """
            Borrar las caracteristicas de un medio de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristica_medio/' +str(self.medio1.id) +'/' ))
        self.selenium.find_element_by_css_selector(
            '#borrar' + str(self.caracteristica1.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_anadir_subcaracteristica(self):
        """
            Test para anadir subcaracteristica de medio de un proyecto.
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristica_medio/' +str(self.medio1.id) +'/' ))
        self.selenium.find_element_by_css_selector(
            '#detalles' + str(self.caracteristica1.id)).click()
        self.selenium.find_element_by_css_selector('#add').click()
        nombre_sub = "nombre_sub"
        self.selenium.find_element_by_name(
            'nombre_sub').send_keys(nombre_sub)
        atributo = "atributo"
        self.selenium.find_element_by_name('atributo').send_keys(atributo)
        comentario = "comentario"
        self.selenium.find_element_by_name('comentario').send_keys(comentario)

    def test_editar_subcaracteristica(self):
        """
            Editar las subcaracteristicas de un medio
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
             '/consultor-crud/caracteristica_medio/detalles/caracteristica/'+str(self.caracteristica1.id) +'/' ))
        self.selenium.find_element_by_css_selector(
            '#editar' + str(self.subcaracteristica1.id)).click()
        atributo = "Edicion de prueba"
        self.selenium.find_element_by_name('atributo').send_keys(atributo)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_eliminar_subcaracteristica(self):
        """
            Borrar las subcaracteristicas de un medio de un proyecto
        """
        self.selenium.get(
            '%s%s' %
            (self.live_server_url,
              '/consultor-crud/caracteristica_medio/detalles/caracteristica/'+str(self.caracteristica1.id) +'/'))
        self.selenium.find_element_by_css_selector('#borrar' + str(self.subcaracteristica1.id)).click()
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

class TestTipoCosto(SeleniumTestCase):
    """
        Clase para probar las vistas del crud del consultor ambiental.
    """

    def setUp(self):
        # Se crea un proyecto para editar y eliminar
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_path = os.path.join(self.base_dir, 'static', 'img', 'germanbb.jpg')
        self.proyecto = DatosProyecto.objects.create(
            titulo="prueba de detalles",
            ubicacion="caracas, venezuela",
            area="area de prueba, caracas",
            tipo="prueba selenium",
            )

        self.proyecto1 = DatosProyecto.objects.create(
            titulo="prueba de detalles1",
            ubicacion="caracas, venezuela1",
            area="area de prueba, caracas1",
            tipo="prueba selenium1")

        self.TipoHumano = TipoCosto.objects.create(
            tipo="humano")

        self.TipoMateriales = TipoCosto.objects.create(
            tipo="materiales")

        self.TipoProfesionales = TipoCosto.objects.create(
            tipo="profesionales")

        self.TipoHospedaje = TipoCosto.objects.create(
            tipo="hospedaje")

        self.TipoOficina = TipoCosto.objects.create(
            tipo="oficina")

        self.TipoInsumos = TipoCosto.objects.create(
            tipo="insumos")

        self.CostoHumano = CostoHumano.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoHumano,
            actividad="actividad realizada",
            cantidad="10 personas",
            tiempo="dos semanas",
            monto=100)

        self.CostoHospedaje = CostoHumano.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoHospedaje,
            actividad="actividad realizada",
            cantidad="10 personas",
            tiempo="dos semanas",
            monto=100)

        self.CostoServicios = CostoHumano.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoProfesionales,
            actividad="actividad realizada",
            cantidad="10 personas",
            tiempo="dos semanas",
            monto=100)

        self.CostoMateriales = CostoMateriales.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoMateriales,
            material="material utilizado",
            cantidad=10,
            costo_unidad=10,
            monto=100)

        self.CostoOficina = CostoMateriales.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoOficina,
            material="material utilizado",
            cantidad=10,
            costo_unidad=10,
            monto=100)

        self.CostoInsumos = CostoMateriales.objects.create(
            proyecto=self.proyecto,
            tipo=self.TipoInsumos,
            material="material utilizado",
            cantidad=10,
            costo_unidad=10,
            monto=100)

        # Se inicia sesion en cada prueba de forma automatica
        self.selenium.get(
            '{}{}'.format(
                self.live_server_url,
                reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

    def test_anadir_costo_humano(self):
        """
            Test para anadir costo humano.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-humano/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        actividad = "Actividades realizadas"
        self.selenium.find_element_by_name('actividad').send_keys(actividad)
        cantidad = "Cantidad de actividades"
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        tiempo = "Tiempo que tardaron"
        self.selenium.find_element_by_name('tiempo').send_keys(tiempo)
        monto = 10
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()
    
    def test_anadir_costo_servicios(self):
        """
            Test para anadir costo de servicios.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-servicio/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        actividad = "Actividades realizadas"
        self.selenium.find_element_by_name('actividad').send_keys(actividad)
        cantidad = "Cantidad de actividades"
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        tiempo = "Tiempo que tardaron"
        self.selenium.find_element_by_name('tiempo').send_keys(tiempo)
        monto = 20
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()
    
    def test_anadir_costo_pasaje(self):
        """
            Test para anadir costo de pasaje.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-pasaje/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        actividad = "Actividades realizadas"
        self.selenium.find_element_by_name('actividad').send_keys(actividad)
        cantidad = "Cantidad de actividades"
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        tiempo = "Tiempo que tardaron"
        self.selenium.find_element_by_name('tiempo').send_keys(tiempo)
        monto = 30
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_anadir_costo_recurso(self):
        """
            Test para anadir costo de recursos.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-recursos/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        material = "Materiales usados"
        self.selenium.find_element_by_name('material').send_keys(material)
        cantidad = 10
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        costo_unidad = 10
        self.selenium.find_element_by_name('costo_unidad').send_keys(costo_unidad)
        monto = 100
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_anadir_costo_oficina(self):
        """
            Test para anadir costo de oficina.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-oficina/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        material = "Materiales usados"
        self.selenium.find_element_by_name('material').send_keys(material)
        cantidad = 20
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        costo_unidad = 20
        self.selenium.find_element_by_name('costo_unidad').send_keys(costo_unidad)
        monto = 400
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_anadir_costo_insumo(self):
        """
            Test para anadir costo de recursos.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultor-crud/costos/nuevo-costo-insumos/'))
        proyecto = self.proyecto1.titulo
        self.selenium.find_element_by_name('proyecto').send_keys(proyecto)
        material = "Materiales usados"
        self.selenium.find_element_by_name('material').send_keys(material)
        cantidad = 30
        self.selenium.find_element_by_name('cantidad').send_keys(cantidad)
        costo_unidad = 30
        self.selenium.find_element_by_name('costo_unidad').send_keys(costo_unidad)
        monto = 900
        self.selenium.find_element_by_name('monto').send_keys(monto)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()
