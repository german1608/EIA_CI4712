'''Test para el crud del consultor '''
from django.test import TestCase
from .forms import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Create your tests here.


class OrganizacionTestCase(TestCase):
    ''' Pruebas para la tabla de organizacion '''

    def setUp(self):
        '''Se crean instancias de organizaciones para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "natural",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        form_organizacion.save()
        form_data['rif'] = "V-25872062-9"
        form_organizacion = OrganizacionCreateForm(data=form_data)
        form_organizacion.save()

    def test_organizacion_crear(self):
        '''Prueba para crear una instancia de una organizacion'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "natural",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-5",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        form_organizacion.save()
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-5")
        self.assertEqual(organizacion.nombre, "Nombre de prueba")

    def test_organizacion_sin_rif(self):
        '''Prueba para crear una instancia de una organizacion sin rif'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "natural",
            'nombre': "Nombre de prueba",
            'rif': "",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

    def test_organizacion_sin_nombre(self):
        '''Prueba para crear una instancia de una organizacion sin nombre'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "natural",
            'nombre': "",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

    def test_organizacion_editar_nombre(self):
        '''Prueba para editar el nombre de una organizacion'''
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        organizacion.nombre = "Nombre de prueba2"
        organizacion.save()
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        self.assertEqual(organizacion.nombre, "Nombre de prueba2")

    def test_organizacion_editar_rif_existente(self):
        '''Prueba para editar el rif de una organizacion. Se intenta
        ingresar un rif que ya esta registrado'''
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        organizacion.rif = "V-25872062-9"
        try:
            organizacion.save()
            self.fail("Se guardo una instancia de un rif que ya existe")
        except BaseException:
            pass

    def test_organizacion_razonSocial_invalida(self):
        '''Prueba para crear una instancia de una organizacion con la razon social invalida'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "hola",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

    def test_organizacion_email_incompleto(self):
        '''Prueba para crear una instancia de una organizacion con el email incompleto'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "juridica",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())
    
    def test_organizacion_rif_incompleto(self):
        '''Prueba para crear una instancia de una organizacion con el rif incompleto'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "juridica",
            'nombre': "Nombre de prueba",
            'rif': "V258720624",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

    def test_organizacion_cedula_incompleta(self):
        '''Prueba para crear una instancia de una organizacion con la cedula incompleta'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "juridica",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())
    
    def test_organizacion_telefono_incompleto(self):
        '''Prueba para crear una instancia de una organizacion con el telefono incompleto'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "juridica",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "041416339",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

    def test_organizacion_editar_nombre_representante_legal(self):
        '''Prueba para editar el nombre del representante legal de una organizacion'''
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        organizacion.nombre_representante_legal = "Giulianne"
        organizacion.save()
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        self.assertEqual(organizacion.nombre_representante_legal, "Giulianne")

    def test_organizacion_editar_cedula(self):
        '''Prueba para editar la cedula del representante legal de una organizacion'''
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        organizacion.cedula_representante_legal = "V-2587206"
        organizacion.save()
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(
            rif="V-25872062-4")
        self.assertEqual(organizacion.cedula_representante_legal, "V-2587206")

    def test_organizacion_eliminar(self):
        '''Prueba para crear una instancia de una organizacion para luego
        eliminarla y despues verificar si se elimino'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "natural",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-5",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodriguez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        form_organizacion.save()
        # pylint: disable=no-member
        organizacion = Organizacion.objects.get(rif="V-25872062-5").delete()
        try:
            org1 = organizacion = Organizacion.objects.get(rif="V-25872062-5")
        except:
            pass

    def test_organizacion_apellido_invalido(self):
        '''Prueba para crear una instancia de una organizacion con el
        apellido del representante legal invalido'''
        form_data = {
            'proyecto': self.proyecto.id,
            'razon_social': "juridica",
            'nombre': "Nombre de prueba",
            'rif': "V-25872062-4",
            'direccion': "Calle ecuador",
            'nombre_representante_legal': "manuel",
            'apellido_representante_legal': "Rodrigu987ez",
            'cedula_representante_legal': "V25872062",
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_organizacion = OrganizacionCreateForm(data=form_data)
        self.assertFalse(form_organizacion.is_valid())

class SolicitanteTestCase(TestCase):
    ''' Pruebas para la tabla de solicitante '''

    def setUp(self):
        '''Se crean instancias de solicitantes para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "Nombre Prueba",
            'apellido': "Apellido Prueba",
            'cedula': "V2587206",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        form_solicitante.save()
        form_data['cedula'] = "V25872060"
        form_data['pasaporte'] = 25872060
        form_solicitante = SolicitanteCreateForm(data=form_data)
        form_solicitante.save()

    def test_solicitante_crear(self):
        '''Prueba para crear una instancia de un solicitante'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        form_solicitante.save()
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V25872062")
        self.assertEqual(solicitante.nombre, "NombrePrueba")

    def test_solicitante_sin_cedula(self):
        '''Prueba para crear una instancia de un solicitante sin cedula'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())

    def test_solicitante_sin_nombre(self):
        '''Prueba para crear una instancia de un solicitante sin nombre'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())

    def test_solicitante_sin_telefono(self):
        '''Prueba para crear una instancia de un solicitante sin telefono'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())

    def test_solicitante_sin_email(self):
        '''Prueba para crear una instancia de un solicitante sin email'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': ""}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())

    def test_solicitante_editar_nombre(self):
        '''Prueba para editar el nombre de un solicitante'''
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V2587206")
        solicitante.nombre = "NombrePrueba2"
        solicitante.save()
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V2587206")
        self.assertEqual(solicitante.nombre, "NombrePrueba2")

    def test_solicitante_editar_ci_existente(self):
        '''Prueba para editar la cedula de un solicitante. Se intenta
        ingresar una cedula que ya esta registrada'''
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V2587206")
        solicitante.cedula = "V25872060"
        try:
            solicitante.save()
            self.fail("Se guardo una instancia de una cedula que ya existe")
        except BaseException:
            pass
    
    def test_solicitante_editar_email(self):
        '''Prueba para editar el nombre de un solicitante'''
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V2587206")
        solicitante.email = "correo@gmail.com"
        solicitante.save()
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(
            cedula="V2587206")
        self.assertEqual(solicitante.email, "correo@gmail.com")

    def test_solicitante_cedula_incompleta(self):
        '''Prueba para crear una instancia de un solicitante con la cedula incompleta'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "25872062",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())
    
    def test_solicitante_telefono_incompleto(self):
        '''Prueba para crear una instancia de un solicitante con el telefono incompleto'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "041416339",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())
    
    def test_solicitante_email_incompleto(self):
        '''Prueba para crear una instancia de un solicitante con el email incompleto'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "04141633989",
            'email': "prueba@gma"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        self.assertFalse(form_solicitante.is_valid())

    def test_solicitante_eliminar(self):
        '''Prueba para eliminar una instancia de un solicitante'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'telefono': "04141633989",
            'email': "prueba@gmail.com"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        form_solicitante.save()
        # pylint: disable=no-member
        solicitante = Solicitante.objects.get(cedula="V25872062").delete()
        try:
            sol1 = solicitante = Solicitante.objects.get(cedula="V25872062")
        except:
            pass

class ResponsableTestCase(TestCase):
    ''' Pruebas para la tabla de solicitante '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "Nombre Prueba",
            'apellido': "Apellido Prueba",
            'cedula': "V2587206",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        form_responsable.save()
        form_data['cedula'] = "V25872060"
        form_data['pasaporte'] = 25872060
        form_responsable = ResponsableCreateForm(data=form_data)
        form_responsable.save()

    def test_responsable_crear(self):
        '''Prueba para crear una instancia de un responsable'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        form_responsable.save()
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V25872062")
        self.assertEqual(responsable.nombre, "NombrePrueba")

    def test_responsable_sin_cedula(self):
        '''Prueba para crear una instancia de un responsable sin cedula'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_sin_nombre(self):
        '''Prueba para crear una instancia de un responsable sin nombre'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_sin_nivelAcademico(self):
        '''Prueba para crear una instancia de un responsable sin nivel academico'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())
    
    def test_responsable_sin_tipoResponsable(self):
        '''Prueba para crear una instancia de un responsable sin tipo de responsable'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': ""}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_editar_nombre(self):
        '''Prueba para editar el nombre de un responsable'''
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V2587206")
        responsable.nombre = "NombrePrueba2"
        responsable.save()
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V2587206")
        self.assertEqual(responsable.nombre, "NombrePrueba2")

    def test_responsable_editar_ci_existente(self):
        '''Prueba para editar la cedula de un responsable. Se intenta
        ingresar una cedula que ya esta registrada'''
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V2587206")
        responsable.cedula = "V25872060"
        try:
            responsable.save()
            self.fail("Se guardo una instancia de una cedula que ya existe")
        except BaseException:
            pass

    def test_responsable_editar_tipoResponsable(self):
        '''Prueba para editar el tipo de un responsable'''
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V2587206")
        responsable.tipo_responsable = "gerente"
        responsable.save()
        # pylint: disable=no-member
        responsable = Responsable.objects.get(
            cedula="V2587206")
        self.assertEqual(responsable.tipo_responsable, "gerente")

    def test_responsable_cedula_incompleta(self):
        '''Prueba para crear una instancia de un responsable con cedula incompleta'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_tipoPersonal_invalido(self):
        '''Prueba para crear una instancia de un responsable con tipo de personal invalido'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "hola"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_apellido_invalido(self):
        '''Prueba para crear una instancia de un responsable con apellido invalido'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "Apellido334Prueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "hola"}
        form_responsable = ResponsableCreateForm(data=form_data)
        self.assertFalse(form_responsable.is_valid())

    def test_responsable_eliminar(self):
        '''Prueba para crear una instancia de un responsable sin nombre'''
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "NombrePrueba",
            'apellido': "ApellidoPrueba",
            'cedula': "V25872062",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        form_responsable.save()
        # pylint: disable=no-member
        responsable = Responsable.objects.get(cedula="V25872062").delete()
        try:
            res1 = responsable = Responsable.objects.get(cedula="V25872062")
        except:
            pass