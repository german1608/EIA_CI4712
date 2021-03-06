'''Test para el crud del consultor '''
# pylint: disable=too-many-lines
from itertools import count
from django.test import TestCase, tag
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .views import MarcoListView, delete_marco_view, MarcoDetailView, MarcoFormView

# Create your tests here.


class OrganizacionTestCase(TestCase):
    ''' Pruebas para la tabla de organizacion '''

    def setUp(self):
        '''Se crean instancias de organizaciones para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="organizacion",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")
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
        organizacion = form_organizacion.save(commit=False)
        organizacion.proyecto = self.proyecto
        organizacion.save()
        form_data['rif'] = "V-25872062-9"
        form_organizacion = OrganizacionCreateForm(data=form_data)
        organizacion = form_organizacion.save(commit=False)
        organizacion.proyecto = self.proyecto
        organizacion.save()

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
        organizacion = form_organizacion.save(commit=False)
        organizacion.proyecto = self.proyecto
        organizacion.save()
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
        organizacion = form_organizacion.save(commit=False)
        organizacion.proyecto = self.proyecto
        organizacion.save()
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
            titulo="solicitante",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "Nombre Prueba",
            'apellido': "Apellido Prueba",
            'cedula': "V2587206",
            'pasaporte': 25872061,
            'telefono': "04141633960",
            'email': "prueba@gmail.ve"}
        form_solicitante = SolicitanteCreateForm(data=form_data)
        solicitante = form_solicitante.save(commit=False)
        solicitante.proyecto = self.proyecto
        solicitante.save()
        form_data['cedula'] = "V25872060"
        form_data['pasaporte'] = 25872060
        form_solicitante = SolicitanteCreateForm(data=form_data)
        solicitante = form_solicitante.save(commit=False)
        solicitante.proyecto = self.proyecto
        solicitante.save()


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
        solicitante = form_solicitante.save(commit=False)
        solicitante.proyecto = self.proyecto
        solicitante.save()
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
        solicitante = form_solicitante.save(commit=False)
        solicitante.proyecto = self.proyecto
        solicitante.save()
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
            titulo="responsable",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba2")
        form_data = {
            'proyecto': self.proyecto.id,
            'nombre': "Nombre Prueba",
            'apellido': "Apellido Prueba",
            'cedula': "V2587206",
            'pasaporte': 25872061,
            'nivel_academico': "Bachiller",
            'tipo_responsable': "EsIA"}
        form_responsable = ResponsableCreateForm(data=form_data)
        responsable = form_responsable.save(commit=False)
        responsable.proyecto = self.proyecto
        responsable.save()
        form_data['cedula'] = "V25872060"
        form_data['pasaporte'] = 25872060
        form_responsable = ResponsableCreateForm(data=form_data)
        responsable = form_responsable.save(commit=False)
        responsable = self.proyecto
        responsable.save()

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
        responsable = form_responsable.save(commit=False)
        responsable.proyecto = self.proyecto
        responsable.save()
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
        responsable = form_responsable.save(commit=False)
        responsable.proyecto = self.proyecto
        responsable.save()
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
            titulo="datosdocumentos",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2007-10-25",
            'ciudad': "Maracay",
            'estado': "Aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        datos = form_datos.save(commit=False)
        datos.proyecto = self.proyecto
        datos.save()

    def test_datosdocumento_crear(self):
        '''Prueba para crear una instancia de datos de documentos'''
        form_data = {
            'proyecto': self.proyecto.id,
            'fecha': "2006-10-25",
            'ciudad': "maracay",
            'estado': "aragua",
            'pais': "Venezuela"}
        form_datos = DatosDocumentoCreateForm(data=form_data)
        datos = form_datos.save(commit=False)
        datos.proyecto = self.proyecto
        datos.save()
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
        datos = form_datos.save(commit=False)
        datos.proyecto = self.proyecto
        datos.save()
        # pylint: disable=no-member
        DatosDocumento.objects.get(fecha="2006-10-25").delete()
        try:
            DatosDocumento.objects.get(fecha="2006-10-25")
        except BaseException:
            pass


@tag('marco')
class MarcoFormTestCase(TestCase):
    """ Caso de pruebas para el formulario de marcos """
    fixtures = ['proyectos.json']
    def setUp(self):
        ''' Crea data inicial para cada prueba '''
        self.proyecto = DatosProyecto.objects.get(pk=2)

    def test_form_existence(self): # pylint: disable=no-self-use
        ''' Prueba la existencia del formulario '''
        MarcoForm()

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


# pylint: disable=no-member, too-few-public-methods
class MarcoHelper:
    '''
    Helper para los tests de marcos
    '''
    tipo_marcos = ['metodologico', 'teorico', 'juridico']

    def login_util(self):
        ''' Utility para loguearnos en las pruebas que lo requieran '''
        consultor_ambiental = get_user_model().objects.get(username='especialistaesia')
        self.client.login(
            username=consultor_ambiental.username, password='jaja1234')
        return consultor_ambiental


@tag('marco')
class MarcoListViewTestCase(MarcoHelper, TestCase):
    '''
    Prueba la vista de listado de los marcos.
    '''
    fixtures = ['groups.json', 'users.json', 'proyectos.json']

    def test_login_required(self):
        '''
        Prueba que la vista tenga sus restricciones de autenticidad
        '''
        login_url = reverse('login')
        for tipo_marco in self.tipo_marcos:
            target_url = reverse('eia_app:lista-marcos', kwargs={
                'tipo': tipo_marco
            })
            response = self.client.post(target_url)
            actual = response
            expected = login_url + '?next=' + target_url
            self.assertRedirects(actual, expected)


    def test_view_existence(self): # pylint: disable=no-self-use
        ''' Prueba existencia de la vista que va a listar los marcos '''
        MarcoListView()

    def test_view_url_correspondence(self):
        '''
        Prueba que la vista que maneja el url de listado de marcos sea el
        dispatch() de MarcoListView
        '''
        # Primero nos logueamos
        self.login_util()

        # Probamos cada posible url
        for tipo_marco in self.tipo_marcos:
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
        for tipo_marco in self.tipo_marcos:
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:lista-marcos', kwargs={
                    'tipo': tipo_marco
                })
                response = self.client.get(target_url)
                self.assertRedirects(response, '{}?next={}'.format(reverse('login'), target_url))

@tag('marco')
class MarcoDeleteViewTestCase(MarcoHelper, TestCase):
    '''
    Prueba la vista de eliminacion de marcos.
    '''
    fixtures = ['groups.json', 'users.json', 'proyectos.json']

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

    def test_view_marco_proyecto_existe_marco_no(self):
        '''
        Prueba que la vista de eliminacion arroje 404 cuando el proyecto exista
        pero este no tenga marco (de cada tipo) a eliminar
        '''
        # Nos logueamos
        self.login_util()
        # Probamos con cada tipo de marco
        for tipo_marco in self.tipo_marcos:
            pk_a_eliminar = 0
            for i in count(0):
                try:
                    proyecto = DatosProyecto.objects.get(pk=i)
                    marco = getattr(proyecto, 'marco_' + tipo_marco)
                    if marco is None:
                        pk_a_eliminar = i
                        break
                except DatosProyecto.DoesNotExist:
                    pass
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:eliminar-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': pk_a_eliminar
                })
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 404, 'El proyecto no existe, pero la vista'
                                                            'de eliminar no retorno 404')

    def test_view_marco_proyecto_existe_marco_tambien(self):
        '''
        Prueba que la vista de eliminacion retorne codigo 200 cuando
        el proyecto que se le pase tenga un marco asociado
        '''
        # Nos logueamos
        self.login_util()
        # Probamos con cada tipo de marco
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            target_url = reverse('eia_app:eliminar-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            response = self.client.get(target_url)
            actual = response.status_code
            expected = 200
            with self.subTest(tipo_marco=tipo_marco):
                self.assertEqual(actual, expected, 'La vista de eliminacion no retorna codigo 200 '
                                                   'cuando el mismo existe y tiene marco asociado')

    def test_view_marco_post_correct(self):
        '''
        Prueba que la vista de eliminacion de marcos elimine
        marcos correctamente cuando se haga el post
        '''
        # Nos logueamos
        self.login_util()
        # Probamos para cada marco
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            # Verificamos que el marco escogido no sea None, es decir
            # que tenga.
            self.assertIsNotNone(getattr(marco, 'marco_' + tipo_marco))
            target_url = reverse('eia_app:eliminar-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            # Hacemos el post para eliminar
            self.client.post(target_url)
            marco.refresh_from_db()
            # Verificamos que sea none ahora
            self.assertIsNone(getattr(marco, 'marco_' + tipo_marco))

    def test_view_marco_post_redirects_to_list(self):
        '''
        Prueba que la vista de eliminacion rediriga a la de listado
        cuando el marco sea eliminado correctamente
        '''
        # Nos logueamos
        self.login_util()
        # Probamos para cada marco
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            # Verificamos que el marco escogido no sea None, es decir
            # que tenga.
            target_url = reverse('eia_app:eliminar-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            # Hacemos el post para eliminar
            response = self.client.post(target_url)
            actual = response
            expected = reverse('eia_app:lista-marcos', kwargs={
                'tipo': tipo_marco
            })
            self.assertRedirects(actual, expected)


@tag('marco')
class MarcoDetailViewTestCase(MarcoHelper, TestCase):
    '''
    Suite de pruebas para la vista de detalles de marcos
    '''
    fixtures = ['groups.json', 'users.json', 'proyectos.json']

    def test_login_required(self):
        '''
        Prueba que la vista sea accedible solamente por usuarios autenticados
        '''
        login_url = reverse('login')
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()

            target_url = reverse('eia_app:detalles-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            response = self.client.post(target_url)
            actual = response
            expected = login_url + '?next=' + target_url
            self.assertRedirects(actual, expected)

    def test_view_url_correspondence(self):
        '''
        Prueba que la vista que maneja el url de edicion de marcos sea
        MarcoDetailView
        '''
        # Primero nos logueamos
        self.login_util()
        # Probamos cada posible url
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:detalles-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': marco.pk
                })
                response = self.client.get(target_url)
                actual = response.resolver_match.func.__name__
                expected = MarcoDetailView.as_view().__name__
                self.assertEqual(actual, expected,
                                 'La vista no corresponde al url')

    def test_proyecto_no_existe(self):
        '''
        Prueba que la vista retorne 404 cuando el proyecto no exista
        '''
        # Primero nos logueamos
        self.login_util()
        for tipo_marco in self.tipo_marcos:
            pk_a_eliminar = 0
            for i in count(0):
                try:
                    DatosProyecto.objects.get(pk=i)
                except DatosProyecto.DoesNotExist:
                    pk_a_eliminar = i
                    break
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:detalles-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': pk_a_eliminar
                })
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 404, 'El proyecto no existe, pero la vista'
                                                            'de detalles no retorno 404')

    def test_proyecto_existe_pero_no_marco(self):
        '''
        Prueba que la vista de detalles arroje 404 cuando el proyecto exista
        pero este no tenga marco (de cada tipo) a eliminar
        '''
        # Nos logueamos
        self.login_util()
        # Probamos con cada tipo de marco
        for tipo_marco in self.tipo_marcos:
            pk_a_eliminar = 0
            for i in count(0):
                try:
                    proyecto = DatosProyecto.objects.get(pk=i)
                    marco = getattr(proyecto, 'marco_' + tipo_marco)
                    if marco is None:
                        pk_a_eliminar = i
                        break
                except DatosProyecto.DoesNotExist:
                    pass
            with self.subTest(tipo_marco=tipo_marco):
                target_url = reverse('eia_app:detalles-marco', kwargs={
                    'tipo': tipo_marco,
                    'pk': pk_a_eliminar
                })
                response = self.client.get(target_url)
                self.assertEqual(response.status_code, 404, 'El proyecto no existe, pero la vista'
                                                            'de eliminar no retorno 404')

    def test_proyecto_existe_marco_tambien(self):
        '''
        Prueba que la vista de detalles retorne codigo 200 cuando
        el proyecto que se le pase tenga un marco asociado
        '''
        # Nos logueamos
        self.login_util()
        # Probamos con cada tipo de marco
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            target_url = reverse('eia_app:detalles-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            response = self.client.get(target_url)
            actual = response.status_code
            expected = 200
            with self.subTest(tipo_marco=tipo_marco):
                self.assertEqual(actual, expected, 'La vista de detalles no retorna codigo 200 '
                                                   'cuando el mismo existe y tiene marco asociado')

    def test_marco_content(self):
        '''
        Prueba que la vista de detalles tenga el contenido del marco y
        el tipo de marco correspondiente
        '''
        # Nos logueamos
        self.login_util()
        # Probamos con cada tipo de marco
        for tipo_marco in self.tipo_marcos:
            marco = DatosProyecto.objects.filter(~Q(**{
                'marco_{}'.format(tipo_marco): None
            })).first()
            target_url = reverse('eia_app:eliminar-marco', kwargs={
                'tipo': tipo_marco,
                'pk': marco.pk
            })
            response = self.client.get(target_url)
            contenido = getattr(marco, 'marco_' + tipo_marco)
            with self.subTest(tipo_marco=tipo_marco):
                self.assertContains(response, contenido)
                self.assertContains(response, marco.titulo)

@tag('marco')
class MarcoFormViewTestCase(MarcoHelper, TestCase):
    '''
    Pruebas unitarias para para la vista de creacion y edicion
    de marcos de proyectos
    '''
    fixtures = ['groups.json', 'users.json', 'proyectos.json']

    def test_url_correspondence_agregar(self):
        '''
        Prueba que el url de la vista de form de marco use la vista
        MarcoFormView
        '''
        self.login_util()
        for tipo_marco in self.tipo_marcos:
            target_url = reverse('eia_app:crear-marco', kwargs={
                'tipo': tipo_marco
            })
            response = self.client.get(target_url)
            actual = response.resolver_match.func.__name__
            expected = MarcoFormView.as_view().__name__
            self.assertEqual(actual, expected, 'La vista de crear marco no es MarcoFormView')

    def test_login_required_agregar(self):
        '''
        Prueba que la vista de form de marco requiera autenticacion
        '''
        login_url = reverse('login')
        for tipo_marco in self.tipo_marcos:
            target_url = reverse('eia_app:crear-marco', kwargs={
                'tipo': tipo_marco
            })
            response = self.client.get(target_url)
            actual = response
            expected = login_url + '?next=' + target_url
            with self.subTest(tipo_marco=tipo_marco):
                self.assertRedirects(actual, expected)
