'''Test para el crud del consultor '''
from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .views import MarcoListView, delete_marco_view
from itertools import count

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


class MarcoFormTestCase(TestCase):
    """ Caso de pruebas para el formulario de marcos """
    fixtures = ['proyectos.json']
    def setUp(self):
        ''' Crea data inicial para cada prueba '''
        self.proyecto = DatosProyecto.objects.get(pk=2)

    def test_form_existence(self): # pylint: disable=no-self-use
        ''' Prueba la existencia del formulario '''
        MarcoForm()

    def test_form_proyecto_field(self):
        ''' Prueba que el campo proyecto tenga como opciones los proyectos del sistema '''
        form = MarcoForm()
        empty_label = form.fields['proyecto'].empty_label
        actual = list(form.fields['proyecto'].choices)
        expected = [
            ('', empty_label),
        ] + list(map(lambda p: (p.pk, p.__str__()), DatosProyecto.objects.all()))
        self.assertEqual(actual, expected, 'Las opciones de MarcoForm.proyecto no son correctas')

    def test_empty_form_validity(self):
        ''' Prueba que el form no sea valido cuando no se le especifica ningun campo '''
        form = MarcoForm({
            'proyecto': '',
            'contenido': ''
        })
        self.assertFalse(form.is_valid(), 'El formulario esta valido cuando no lo esta')

    def test_form_contenido(self):
        ''' Prueba que el form sea invalido si le falta solo la descripcion '''
        form = MarcoForm({
            'proyecto': str(self.proyecto.pk),
            'contenido': ''
        })
        self.assertFalse(
            form.is_valid(), 'El formulario dijo estar valido cuando no lo esta')

        # Verificamos que el error no haya sido por el campo proyecto
        with self.assertRaises(KeyError):
            print(form.errors['proyecto'])


    def test_form_proyecto_empty(self):
        ''' Prueba que el form sea invalido cuando no se le pase un proyecto '''
        form = MarcoForm({
            'proyecto': '',
            'contenido': 'Contenido'
        })
        # Prueba invalidez
        self.assertFalse(
            form.is_valid(), 'El formulario eta valido cuando no lo esta (falta proyecto)'
        )
        # Prueba que la razon de que haya fallado no haya sido por el contenido
        with self.assertRaises(KeyError):
            print(form.errors['contenido'])

    def test_form_proyecto_invalid_choice(self):
        ''' Prueba que el form sea invalido cuando se le pase un proyecto que no exista '''
        # Guardamos el pk y lo eliminamos
        proyecto_key = self.proyecto.pk
        self.proyecto.delete()
        form = MarcoForm({
            'proyecto': str(proyecto_key),
            'contenido': 'contenido'
        })
        # Prueba invalidez
        self.assertFalse(
            form.is_valid(), 'El formulario esta valido cuando no lo esta (el proyecto no existe)')
        # Prueba que la razon de que haya fallado no haya sido por el contenido
        with self.assertRaises(KeyError):
            print(form.errors['contenido'])

    def test_form_proyecto_valido(self):
        ''' Prueba que el form sea valido cuando se le pasen todos los datos obligatorios '''
        form = MarcoForm({
            'proyecto': self.proyecto.pk,
            'contenido': 'Contenido'
        })
        # Prueba validez
        self.assertTrue(
            form.is_valid(), 'El formulario esta invalido cuando debe estar valido'
        )


class MarcoHelper:
    '''
    Helper para los tests de marcos
    '''
    def login_util(self):
        ''' Utility para loguearnos en las pruebas que lo requieran '''
        consultor_ambiental = get_user_model().objects.get(username='especialistaesia')
        self.client.login(
            username=consultor_ambiental.username, password='jaja1234')
        return consultor_ambiental


class MarcoListViewTestCase(MarcoHelper, TestCase):
    '''
    Prueba la vista de listado de los marcos.
    '''
    fixtures = ['users-and-groups.json', 'proyectos.json']

    def test_view_existence(self): # pylint: disable=self-no-use
        ''' Prueba existencia de la vista que va a listar los marcos '''
        MarcoListView()

    def test_view_url_correspondence(self):
        ''' Prueba que la vista que maneja el url de listado de marcos sea el dispatch() de MarcoListView '''
        # Primero nos logueamos
        self.login_util()

        # Probamos cada posible url
        for tipo_marco in ['metodologico', 'teorico', 'juridico']:
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:lista-marcos', kwargs={
                    'tipo': tipo_marco
                })
                response = self.client.get(target_url)
                actual = response.resolver_match.func.__name__
                expected = MarcoListView.as_view().__name__
                self.assertEqual(actual, expected, 'La vista no corresponde al url')

    def test_vista_redirige_cuando_no_esta_autenticado(self):
        ''' Prueba que la vista rediriga al login si el usuario no esta autenticado '''
        # Hacemos get del url que lista
        for tipo_marco in ['metodologico', 'teorico', 'juridico']:
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:lista-marcos', kwargs={
                    'tipo': tipo_marco
                })
                response = self.client.get(target_url)
                self.assertRedirects(response, '{}?next={}'.format(reverse('login'), target_url))

    def test_vista_muestra_listado_correcto(self):
        ''' Prueba que primero autentica al usuario y luego lo redirige a '''
        # Nos logueamos
        self.login_util()

        # Verificamos el listado de cada marco
        for tipo_marco in ['metodologico', 'teorico', 'juridico']:
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:lista-marcos', kwargs={
                    'tipo': tipo_marco
                })
                response = self.client.get(target_url)
                actual = response.context['object_list']
                expected = DatosProyecto.objects.filter(~Q(**{
                    'marco_{}'.format(tipo_marco): None
                }))
                self.assertEqual(list(actual), list(expected), 'El filtro de la vista de listado de marcos no esta funcionando')

class MarcoDeleteViewTestCase(MarcoHelper, TestCase):
    '''
    Prueba la vista de eliminacion de marcos.
    '''
    fixtures = ['users-and-groups.json', 'proyectos.json']
    tipo_marcos = ['metodologico', 'teorico', 'juridico']

    def test_view_url_correspondence(self):
        '''
        Prueba que la vista que maneja el url de listao de marcos sea
        delete_marco_view
        '''
        # Primero nos logueamos
        self.login_util()
        # Probamos cada posible url
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:eliminar-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': marco.pk
                })
                response = self.client.get(target_url)
                actual = response.resolver_match.func.__name__
                expected = delete_marco_view.__name__
                self.assertEqual(actual, expected, 'La vista no corresponde al url')

    def test_view_marco_proyecto_no_existe(self):
        '''
        Prueba que la vista que maneja el url de listado responda
        con un 404 cuando el proyecto con el marco asociado no exista
        '''
        # Priemro nos logueamos
        self.login_util()
        # Probamos cada posible url
        for tipo_marco in self.tipo_marcos:
            pk_a_eliminar = 0
            for i in count(0):
                try:
                    DatosProyecto.objects.get(pk=i)
                except DatosProyecto.DoesNotExist:
                    pk_a_eliminar = i
                    break

            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:eliminar-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': pk_a_eliminar
                })
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 404, 'El proyecto no existe, pero la vista'
                                                            'de eliminar no retorno 404')
