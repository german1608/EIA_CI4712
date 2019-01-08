''' Continuacion de pruebas '''
from django.test import TestCase
from .forms import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .models import *  # pylint: disable=wildcard-import, unused-wildcard-import


class MedioTestCase(TestCase):
    ''' Pruebas para la tabla de medio de un proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="hola2",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")

    def test_medio_crear(self):
        '''Prueba para crear una instancia de datos de medio'''
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
        # pylint: disable=no-member
        datos = Medio.objects.get(
            proyecto=self.proyecto.id)
        self.assertEqual(datos.tipo, "fisico")

    def test_medio_sin_tipo(self):
        '''Prueba para crear una instancia de medio sin tipo'''
        form_data = {
            'tipo': '',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_tipo_invalido(self):
        '''Prueba para crear una instancia de medio con tipo invalido'''
        form_data = {
            'tipo': 'otro',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_sin_descripcion(self):
        '''Prueba para crear una instancia de medio sin descripcion'''
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': '',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_medio_sin_conclusion(self):
        '''Prueba para crear una instancia de medio sin conclusion'''
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': ''}
        form_datos = MedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_medio_editar_tipo(self):
        '''Prueba para editar el tipo de medio por un medio valido'''
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
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
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
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
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
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
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
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
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba',
            'conclusiones': 'esto es una conclusion'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
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
        self.proyecto = DatosProyecto.objects.create(
            titulo="caracteristicas",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba de medio',
            'conclusiones': 'esto es una conclusion de medio'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
        self.medio = Medio.objects.get(proyecto=self.proyecto.id, tipo='fisico')

    def test_caracteristica_medio_crear(self):
        '''Prueba para crear una instancia de datos de caracteristica de medio'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': self.medio.id,
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='esto es una caracteristica')
        self.assertEqual(datos.caracteristica, 'esto es una caracteristica')

    def test_caracteristica_medio_sin_medio(self):
        '''Prueba para crear una instancia de caracteristica de medio sin medio'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': '',
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_caracteristica_medio_sin_caracteristica(self):
        '''Prueba para crear una instancia de caracteristica de medio sin caracteristica'''
        form_data = {
            'caracteristica': '',
            'medio': self.medio.id,
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_caracteristica_medio_sin_descripcion(self):
        '''Prueba para crear una instancia de caracteristica de medio sin descripcion'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': self.medio.id,
            'descripcion': ''
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_caracteristica_medio_editar_caracteristica(self):
        '''Prueba para editar la caracteristica'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': self.medio.id,
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='esto es una caracteristica')
        datos.caracteristica = 'oops'
        datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='oops')
        self.assertEqual(datos.caracteristica, "oops")

    def test_caracteristica_medio_editar_descripcion(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': self.medio.id,
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='esto es una caracteristica')
        datos.descripcion = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='esto es una caracteristica')
        self.assertEqual(datos.descripcion, "oops")

    def test_caracteristica_medio_eliminar(self):
        '''Prueba para eliminar una instancia de caracteristica de medio'''
        form_data = {
            'caracteristica': 'esto es una caracteristica',
            'medio': self.medio.id,
            'descripcion': 'esto es una prueba'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        CaracteristicaMedio.objects.get(
            medio=self.medio.id, caracteristica='esto es una caracteristica').delete()
        try:
            CaracteristicaMedio.objects.get(medio=self.medio)
        except BaseException:
            pass


class SubaracteristicaMedioTestCase(TestCase):
    ''' Pruebas para la tabla de subcaracteristicas del medio de un proyecto '''

    def setUp(self):
        '''Se crean instancias de responsables para realizar pruebas'''
        # pylint: disable=no-member
        self.proyecto = DatosProyecto.objects.create(
            titulo="subcaracteristicas",
            ubicacion="caracas",
            area="area de prueba",
            tipo="prueba")
        form_data = {
            'tipo': 'fisico',
            'proyecto': self.proyecto.id,
            'descripcion': 'esto es una prueba de medio',
            'conclusiones': 'esto es una conclusion de medio'}
        form_datos = MedioCreateForm(data=form_data)
        medio = form_datos.save(commit=False)
        medio.proyecto = self.proyecto
        medio.save()
        medio = Medio.objects.get(proyecto=self.proyecto.id, tipo='fisico')
        form_data = {
            'caracteristica': 'esto es una caracteristica de caracteristicamedio',
            'medio': medio.id,
            'descripcion': 'esto es una prueba de caracteristicamedio'
        }
        form_datos = CaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        self.caracteristica = CaracteristicaMedio.objects.get(
            medio=medio.id,
            caracteristica='esto es una caracteristica de caracteristicamedio')

    def test_subcaracteristica_medio_crear(self):
        '''Prueba para crear una instancia de datos de subcaracteristica'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        self.assertEqual(datos.nombre_sub, 'nombre')

    def test_subcaracteristica_medio_sin_nombre(self):
        '''Prueba para crear una instancia de subcaracteristica sin nombre'''
        form_data = {
            'nombre_sub': '',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_caracteristica(self):
        '''Prueba para crear una instancia de subcaracteristica sin caracteristica'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': '',
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_atributo(self):
        '''Prueba para crear una instancia de subcaracteristica sin atributo'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': '',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    def test_subcaracteristica_medio_sin_comentario(self):
        '''Prueba para crear una instancia de subcaracteristica sin comentario'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': ''
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        self.assertFalse(form_datos.is_valid())

    # pylint: disable=invalid-name
    def test_subcaracteristica_medio_editar_nombre(self):
        '''Prueba para editar la caracteristica'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        datos.nombre_sub = 'oops'
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='oops')
        self.assertEqual(datos.nombre_sub, "oops")

    def test_subcaracteristica_medio_editar_atributo(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        datos.atributo = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        self.assertEqual(datos.atributo, "oops")

    def test_subcaracteristica_medio_editar_comentario(self):
        '''Prueba para editar la descripcion'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        datos.comentario = "oops"
        datos.save()
        # pylint: disable=no-member
        datos = SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre')
        self.assertEqual(datos.comentario, "oops")

    def test_subcaracteristica_medio_eliminar(self):
        '''Prueba para eliminar una instancia de caracteristica de medio'''
        form_data = {
            'nombre_sub': 'nombre',
            'caracteristica': self.caracteristica.id,
            'atributo': 'atributo',
            'comentario': 'comentario'
        }
        form_datos = SubaracteristicaMedioCreateForm(data=form_data)
        form_datos.save()
        # pylint: disable=no-member
        SubaracteristicaMedio.objects.get(
            caracteristica=self.caracteristica.id, nombre_sub='nombre').delete()
        try:
            SubaracteristicaMedio.objects.get(
                caracteristica=self.caracteristica.id, nombre_sub='nombre')
        except BaseException:
            pass
