'''Test para el crud del consultor '''
from django.test import TestCase
from .forms import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import
import os

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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
    def test_organizacion_razonsocial_invalida(self):
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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
        Organizacion.objects.get(rif="V-25872062-5").delete()
        try:
            Organizacion.objects.get(rif="V-25872062-5")
        except BaseException:
            pass

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
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
        Solicitante.objects.get(cedula="V25872062").delete()
        try:
            Solicitante.objects.get(cedula="V25872062")
        except BaseException:
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

    # pylint: disable=invalid-name
    def test_responsable_sin_nivelacademico(self):
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

    # pylint: disable=invalid-name
    def test_responsable_sin_tiporesponsable(self):
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
    def test_responsable_editar_tiporesponsable(self):
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

    # pylint: disable=invalid-name
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

    # pylint: disable=invalid-name
    def test_responsable_tipopersonal_invalido(self):
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

    # pylint: disable=invalid-name
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
        '''Prueba para eliminar una instancia de un responsable'''
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
        Responsable.objects.get(cedula="V25872062").delete()
        try:
            Responsable.objects.get(cedula="V25872062")
        except BaseException:
            pass


class DatosDocumentoTestCase(TestCase):
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
            'fecha': "2007-10-25",
            'ciudad': "Maracay",
            'estado': "Aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        form_datos.save()

    def test_datosdocumento_crear(self):
        '''Prueba para crear una instancia de datos de documentos'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "maracay",
            'estado': "aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2006-10-25")
        self.assertEqual(datos.ciudad, "maracay")

    def test_datosdocumento_sin_fecha(self):
        '''Prueba para crear una instancia de datos de documentos sin fecha'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "",
            'ciudad': "maracay",
            'estado': "aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_datosdocumento_sin_ciudad(self):
        '''Prueba para crear una instancia de datos de documentos sin ciudad'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "",
            'estado': "aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_datosdocumento_sin_estado(self):
        '''Prueba para crear una instancia de datos de documentos sin estado'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "maracay",
            'estado': "",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_datosdocumento_sin_pais(self):
        '''Prueba para crear una instancia de datos de documentos sin pais'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "maracay",
            'estado': "aragua",
            'pais': ""}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_datosdocumento_editar_ciudad(self):
        '''Prueba para editar la ciudad de un documento'''
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        datos.ciudad = "Caracas"
        datos.save()
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        self.assertEqual(datos.ciudad, "Caracas")

    # pylint: disable=invalid-name
    def test_datosdocumento_editar_estado(self):
        '''Prueba para editar el estado de un documento'''
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        datos.ciudad = "Miranda"
        datos.save()
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        self.assertEqual(datos.ciudad, "Miranda")

    def test_datosdocumento_editar_pais(self):
        '''Prueba para editar el pais de un documento'''
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        datos.pais = "España"
        datos.save()
        # pylint: disable=no-member
        datos = DatosDocumento.objects.get(
            fecha="2007-10-25")
        self.assertEqual(datos.pais, "España")

    def test_datosdocumento_eliminar(self):
        '''Prueba para eliminar una instancia de datos de documentos'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "maracay",
            'estado': "aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        DatosDocumento.objects.get(fecha="2006-10-25").delete()
        try:
            DatosDocumento.objects.get(fecha="2006-10-25")
        except BaseException:
            pass
""" 
class DescripcionProyectoTestCase(TestCase):
    ''' Pruebas para la tabla de Descripcion proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.img_path = os.path.join(BASE_DIR, 'static', 'img','germanbb.jpg')
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")

    def test_DescripcionProyecto_crear(self):
        '''Prueba para crear una instancia de descripcion proyecto'''
        img = SimpleUploadedFile(name='german.jpg', content=open(self.img_path, 'rb').read(), content_type='image/jpeg')
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : 'ObjGeneral',
            'obj_especifico' : 'ObjEspecifico',
            'justificacion' : 'Porque quise'}
        file_data = {'area':SimpleUploadedFile('germanbb.jpg', 'area')}
        form_datos = DescripcionProyectoCreateForm(form_data,file_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.obj_general, "ObjGeneral")

    def test_DescripcionProyecto_sin_objetivo_general(self):
        '''Prueba para crear una instancia sin objetivo general'''
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : '',
            'obj_especifico' : 'ObjEspecifico',
            'justificacion' : 'Porque quise',
            'area' : SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')}
        form_datos = DescripcionProyectoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_DescripcionProyecto_sin_objetivo_especifico(self):
        '''Prueba para crear una instancia sin objetivo especifico'''
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : 'ObjGeneral',
            'obj_especifico' : '',
            'justificacion' : 'Porque quise',
            'area' : SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')}
        form_datos = DescripcionProyectoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_DescripcionProyecto_sin_justificacion(self):
        '''Prueba para crear una instancia sin justificacion'''
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : 'ObjGeneral',
            'obj_especifico' : 'ObjEspecifico',
            'justificacion' : '',
            'area' : SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')}
        form_datos = DescripcionProyectoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_DescripcionProyecto_sin_area(self):
        '''Prueba para crear una instancia sin area'''
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : 'ObjGeneral',
            'obj_especifico' : 'ObjEspecifico',
            'justificacion' : 'Porque quise',
            'area' : None}
        form_datos = DescripcionProyectoCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_DescripcionProyecto_editar_obj_general(self):
        '''Prueba para editar el objetivo general de un documento'''
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        datos.obj_general = "Ya basta wei"
        datos.save()
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.obj_general, "Ya basta wei")

    # pylint: disable=invalid-name
    def test_DescripcionProyecto_editar_obj_especifico(self):
        '''Prueba para editar el objetivo especifico de un documento'''
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        datos.obj_especifico = "Ya basta wei"
        datos.save()
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.obj_especifico, "Ya basta wei")

    # pylint: disable=invalid-name
    def test_DescripcionProyecto_editar_justificacion(self):
        '''Prueba para editar la justificacion'''
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        datos.justificacion = "Ya basta wei"
        datos.save()
        # pylint: disable=no-member
        datos = DescripcionProyecto.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.justificacion, "Ya basta wei")

    def test_DescripcionProyecto_eliminar(self):
        '''Prueba para eliminar una instancia'''
        form_data = {
            'proyecto': self.proyecto.id,
            'obj_general' : 'ObjGeneral',
            'obj_especifico' : 'ObjEspecifico',
            'justificacion' : 'Porque quise',
            'area' : SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')}
        form_datos = DescripcionProyectoCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        DescripcionProyecto.objects.get(proyecto=self.proyecto.id).delete()
        try:
            DescripcionProyecto.objects.get(proyecto=self.proyecto.id)
        except BaseException:
            pass """

class MedioTestCase(TestCase):
    ''' Pruebas para la tabla de medio de un proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")

    def test_medio_crear(self):
        '''Prueba para crear una instancia de datos de medio'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.tipo, "fisico")

    def test_medio_sin_proyecto(self):
        '''Prueba para crear una instancia de medio sin proyecto'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : None,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_sin_tipo(self):
        '''Prueba para crear una instancia de medio sin tipo'''
        form_data = {
            'tipo' : '',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_tipo_invalido(self):
        '''Prueba para crear una instancia de medio con tipo invalido'''
        form_data = {
            'tipo' : 'otro',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_sin_descripcion(self):
        '''Prueba para crear una instancia de medio sin descripcion'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : '',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_sin_conclusion(self):
        '''Prueba para crear una instancia de medio sin conclusion'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : ''}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())
 
    # pylint: disable=invalid-name
    def test_medio_editar_tipo(self):
        '''Prueba para editar el tipo de medio por un medio valido'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        datos.tipo = "biologico"
        datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.tipo, "biologico")

    def test_medio_editar_tipo_invalido(self):
        '''Prueba para editar el tipo de medio por un medio invalido'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        datos.tipo = "otro"
        try:
            datos.save()
        except BaseException:
            pass

    # pylint: disable=invalid-name
    def test_medio_editar_descripcion(self):
        '''Prueba para editar la descripcion del medio'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        datos.descripcion = "Esta es otra prueba"
        datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.descripcion, "Esta es otra prueba")

    def test_medio_editar_conclusion(self):
        '''Prueba para editar las conclusiones del medio'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        datos.conclusiones = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.conclusiones, "oops") 
        
    def test_medio_eliminar(self):
        '''Prueba para eliminar una instancia de medio'''
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : self.proyecto.id,
            'descripcion' : 'esto es una prueba',
            'conclusiones' : 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        Medio.objects.get(proyecto=self.proyecto.id).delete()
        try:
            Medio.objects.get(proyecto=self.proyecto.id)
        except BaseException:
            pass

class CaracteristicaMedioTestCase(TestCase):
    ''' Pruebas para la tabla de caracteristicas del medio de un proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : proyecto.id,
            'descripcion' : 'esto es una prueba de medio',
            'conclusiones' : 'esto es una conclusion de medio'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        self.medio=Medio.objects.get(proyecto=proyecto.id,tipo='fisico')

    def test_caracteristica_medio_crear(self):
        '''Prueba para crear una instancia de datos de caracteristica de medio'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : self.medio.id,
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='esto es una caracteristica')
        self.assertEqual(datos.caracteristica, 'esto es una caracteristica')

    def test_caracteristica_medio_sin_medio(self):
        '''Prueba para crear una instancia de caracteristica de medio sin medio'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : '',
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_caracteristica_medio_sin_caracteristica(self):
        '''Prueba para crear una instancia de caracteristica de medio sin caracteristica'''
        form_data = {
            'caracteristica' : '',
            'medio' : self.medio.id,
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_caracteristica_medio_sin_descripcion(self):
        '''Prueba para crear una instancia de caracteristica de medio sin descripcion'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : self.medio.id,
            'descripcion' : ''
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_caracteristica_medio_editar_caracteristica(self):
        '''Prueba para editar la caracteristica'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : self.medio.id,
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='esto es una caracteristica')
        datos.caracteristica = 'oops'
        datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='oops')
        self.assertEqual(datos.caracteristica, "oops")

    def test_caracteristica_medio_editar_descripcion(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : self.medio.id,
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='esto es una caracteristica')
        datos.descripcion = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='esto es una caracteristica')
        self.assertEqual(datos.descripcion, "oops")

    def test_caracteristica_medio_eliminar(self):
        '''Prueba para eliminar una instancia de caracteristica de medio'''
        form_data = {
            'caracteristica' : 'esto es una caracteristica',
            'medio' : self.medio.id,
            'descripcion' : 'esto es una prueba'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        CaracteristicaMedio.objects.get(
            medio=self.medio.id,caracteristica='esto es una caracteristica').delete()
        try:
            CaracteristicaMedio.objects.get(medio=self.medio)
        except BaseException:
            pass 

class SubaracteristicaMedioTestCase(TestCase):
    ''' Pruebas para la tabla de subcaracteristicas del medio de un proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        proyecto = DatosProyecto.objects.create(
            titulo="hola",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba",
            url="www.google.com")
        form_data = {
            'tipo' : 'fisico',
            'proyecto' : proyecto.id,
            'descripcion' : 'esto es una prueba de medio',
            'conclusiones' : 'esto es una conclusion de medio'}
        form_datos = MedioCreateForm(data=form_data)
        form_datos.save()
        medio=Medio.objects.get(proyecto=proyecto.id,tipo='fisico')
        form_data = {
            'caracteristica' : 'esto es una caracteristica de caracteristicamedio',
            'medio' : medio.id,
            'descripcion' : 'esto es una prueba de caracteristicamedio'
            }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        self.caracteristica = CaracteristicaMedio.objects.get(
            medio=medio.id,
            caracteristica='esto es una caracteristica de caracteristicamedio')

    def test_subcaracteristica_medio_crear(self):
        '''Prueba para crear una instancia de datos de subcaracteristica'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        self.assertEqual(datos.nombre_sub, 'nombre')

    def test_subcaracteristica_medio_sin_nombre(self):
        '''Prueba para crear una instancia de subcaracteristica sin nombre'''
        form_data = {
            'nombre_sub' : '',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_caracteristica(self):
        '''Prueba para crear una instancia de subcaracteristica sin caracteristica'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : '',
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_atributo(self):
        '''Prueba para crear una instancia de subcaracteristica sin atributo'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : '',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_comentario(self):
        '''Prueba para crear una instancia de subcaracteristica sin comentario'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : ''
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_subcaracteristica_medio_editar_nombre(self):
        '''Prueba para editar la caracteristica'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        datos.nombre_sub = 'oops'
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='oops')
        self.assertEqual(datos.nombre_sub, "oops")

    def test_subcaracteristica_medio_editar_atributo(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        datos.atributo = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        self.assertEqual(datos.atributo, "oops")

    def test_subcaracteristica_medio_editar_comentario(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        datos.comentario = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre')
        self.assertEqual(datos.comentario, "oops")

    def test_subcaracteristica_medio_eliminar(self):
        '''Prueba para eliminar una instancia de caracteristica de medio'''
        form_data = {
            'nombre_sub' : 'nombre',
            'caracteristica' : self.caracteristica.id,
            'atributo' : 'atributo',
            'comentario' : 'comentario'
            }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id,nombre_sub='nombre').delete()
        try:
            SubaracteristicaMedio.objects.get(
                caracteristica=self.caracteristica.id,nombre_sub='nombre')
        except BaseException:
            pass 