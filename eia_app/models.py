"""
    Archivo con todos los modelos necesarios
    para la creacion de un EsIA.
"""

import re
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _  # pylint: disable=unused-import
from eia.validators import CI_VALIDATOR


class DatosProyecto(models.Model):
    """ Tabla para almacenar la informacion general de un proyecto.
    Parametros:
        models.Model (DatosProyecto): Instancia sobre la que se crea la tabla.
    Atributos:
        titulo: Titulo del proyecto
        ubicacion: ubicacion geografica donde se desarrollara el proyecto
        area: area de desempeño del proyecto
        tipo: tipo de proyecto
        url: Url al PDF del proyecto.
    """
    titulo = models.CharField(max_length=100, unique=True)
    ubicacion = models.TextField()
    area = models.TextField()
    tipo = models.TextField()
    marco_metodologico = models.TextField(null=True)
    marco_juridico = models.TextField(null=True)
    marco_teorico = models.TextField(null=True)

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Datos_Proyecto"

    def __str__(self):
        '''Devuelve el nombre del proyecto'''
        return str(self.titulo)


class DatosPersona(models.Model):
    """ Tabla para registrar los datos de un representante legal
        de una organizacion.
        Parametros:
            models.Model (Representante_legal): Instancia sobre la que
            se crea la tabla.
        Atributos:
            nombre: Nombre del representante legal
            apellido: Apellido del representante legal
            cedula: Cedula del representante legal
            pasaporte: pasaporte del represenante legal
    """
    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre pasporte y cedula'''
        unique_together = (('cedula', 'pasaporte'))
    nombre = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula = models.CharField(
        max_length=8,
        validators=[CI_VALIDATOR])
    pasaporte = models.IntegerField(validators=[MinValueValidator(0)])


class Organizacion(models.Model):
    """ Tabla de las organizaciones que proponen un proyecto
    al EsIA.
    Parametros:
        models.Model (Organizacion): Instancia sobre la que se
        crea la tabla.
    Atributos de la clase:
        proyecto: proyecto al que pertenece la organizacion
        razon_social: Razon social de la organizacion
        nombre: Nombre de la orgnizacion
        rif: Rif de la organizacion
        direccion: direccion de la organizacion
        representante_legal: Datos del representante legal de la organizacion
        telefono: Telefono de la organizacion
        email: Email de la organizacion
    """
    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    RAZON_SOCIAL_CHOICES = (('natural', 'Persona natural'),
                            ('juridica', 'Persona Jurídica'))
    razon_social = models.CharField(max_length=8, choices=RAZON_SOCIAL_CHOICES)
    nombre = models.CharField(max_length=100)
    rif = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                re.compile('^([VEJPGvejpg]{1})-([0-9]{8})-([0-9]{1}$)'),
                _('RIF incorrecto'),
                'invalid')])
    direccion = models.TextField()
    nombre_representante_legal = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido_representante_legal = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_representante_legal = models.CharField(
        max_length=9,
        validators=[CI_VALIDATOR])
    pasaporte_representante_legal = models.IntegerField(
        validators=[MinValueValidator(0)], blank=True, null=True)
    telefono = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                (re.compile('^[0-9]{11}$')),
                _('Teléfono incorrecto'),
                'invalid')])
    email = models.EmailField()

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Organizacion"


class Solicitante(models.Model):
    """ Tabla para almacenar los datos de un solicitante
    o promotor del proyecto.
    Parametros:
        models.Model (Solicitante): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: proyecto al que pertenece el solicitante
        nombre: Nombre del solicitante o promotor
        apellido: Apellido del solicitante o promotor
        cedula: Cedula del solicitante o promotor
        pasaporte: pasaporte del solicitante o promotor
        telefono: Telefono del solicitante o promotor
        email: Email del solicitante o promotor
    """
    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre pasporte y cedula'''
        unique_together = (('cedula', 'pasaporte'))

    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula = models.CharField(
        max_length=9,
        validators=[CI_VALIDATOR])
    pasaporte = models.IntegerField(
        validators=[
            MinValueValidator(0)],
        blank=True,
        null=True)
    telefono = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                (re.compile('^[0-9]{11}$')),
                _('Teléfono incorrecto'),
                'invalid')])
    email = models.EmailField()

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Solicitante"


class Responsable(models.Model):
    """ Tabla para almacenar los datos de una persona
    responsable de un proyecto.
    Parametros:
        models.Model (Solicitante): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: proyecto al que pertenece el responsable
        nombre: Nombre del responsable
        apellido: Apellido del responsable
        cedula: Cedula del responsable
        pasaporte: pasaporte del responsable
                nivel_academico: Nivel academico del responsable
        tipo_responsable: Tipo de especialidad del responsable
    """
    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre pasporte y cedula'''
        unique_together = (('cedula', 'pasaporte'))

    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula = models.CharField(
        max_length=9,
        validators=[CI_VALIDATOR])
    pasaporte = models.IntegerField(
        validators=[
            MinValueValidator(0)],
        blank=True,
        null=True)
    nivel_academico = models.CharField(max_length=100)
    TIPO_PERSONAL = (('EsIA', 'Especialista del EsIA'),
                     ('fisico', 'Especialista del Medio Físico'),
                     ('biologico', 'Especialista del Medio Biológico'),
                     ('socioeconomico', 'Especialista del Medio Socioeconómico'),
                     ('gerente', 'Gerente del Proyecto de Desarrollo'))
    tipo_responsable = models.CharField(max_length=16, choices=TIPO_PERSONAL)

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Responsable"


class DatosDocumento(models.Model):
    """ Tabla para almacenar la informacion de los datos de un documento de intencion.
    Parametros:
        models.Model (DatosDocumento): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: Proyecto al que pertenencen los datos del documento.
        fecha: fecha en que se realiza el estudio
        ciudad: ciudad donde se realiza el estudio
        estado: estado donde se realiza el estudio
        pais: pais donde se realiza el estudio
    """
    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Datos_Documento"


class DescripcionProyecto(models.Model):
    """ Tabla para almacenar la informacion de la descripcion de un proyecto.
    Parametros:
        models.Model (DescripcionProyecto): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: Proyecto al que pertenencen los datos del documento.
        objGeneral: objetivo general del estudio
        objEspecifico: objetivos especificos del estudio
        justificacion: azones por las que se realiza el estudio
        area: mapa del sitio o espacio donde se realiza el estudio
    """
    proyecto = models.OneToOneField(DatosProyecto, on_delete=models.CASCADE)
    obj_general = models.TextField()
    obj_especifico = models.TextField()
    justificacion = models.TextField()
    area = models.ImageField()

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Descripcion_Proyecto"

class RecomendacionProyecto(models.Model):
    """ Tabla para almacenar la informacion de las recomendaciones de un proyecto"""
    proyecto = models.OneToOneField(DatosProyecto, on_delete=models.CASCADE)
    recomendaciones = models.TextField()

class ConclusionProyecto(models.Model):
    """ Tabla para alamacenar la informacion de las conclusiones de un proyecto """
    proyecto = models.OneToOneField(DatosProyecto, on_delete=models.CASCADE)
    conclusiones = models.TextField()

class Medio(models.Model):
    """ Tabla para almacenar la informacion del medio de un proyecto.
    Parametros:
        models.Model (Medio): Instancia sobre la que se crea la tabla.
    Atributos:
        tipo: Tipo de medio
        proyecto: Proyecto asociado
        descripcion: Descripcion del medio
        conclusiones: Conclusiones sobre el medio
    """

    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre tipo y proyecto'''
        unique_together = (('tipo', 'proyecto'))

    TYPE_CHOICES = (('fisico', 'Medio físico'),
                    ('biologico', 'Medio biológico'),
                    ('socio', 'Medio sociocultural'))
    tipo = models.CharField(max_length=100, choices=TYPE_CHOICES)
    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    conclusiones = models.TextField()

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "Medio"


class CaracteristicaMedio(models.Model):
    """ Tabla para almacenar las caracteristicas de un medio fisico de un proyecto.
    Parametros:
        models.Model (CaracteristicaMedio): Instancia sobre la que se crea la tabla.
    Atributos:
        tipo: Nombre de la caracteristica asociada al medio fisico
        proyecto: Proyecto asociado
    """
    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre tipo y proyecto'''
        unique_together = (('caracteristica', 'medio'))

    caracteristica = models.CharField(max_length=100)
    medio = models.ForeignKey(Medio, on_delete=models.CASCADE)
    descripcion = models.TextField(default="")

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "CaracteristicaMedio"


class SubaracteristicaMedio(models.Model):
    """ Tabla para almacenar las caracteristicas de un medio fisico de un proyecto.
    Parametros:
        models.Model (SubaracteristicaMedio): Instancia sobre la que se crea la tabla.
    Atributos:
        nombre_sub: Nombre de la subcaracteristica asociada a la caracteristica
        caracteristica: caracteristica asociada
        atributo: especificaciones de la subcaracteristica
        comentario: comentarios adicionales de la subcaracteristica
    """
    class Meta:  # pylint: disable=too-few-public-methods
        '''Hacer unica la combinacion entre tipo y proyecto'''
        unique_together = (('nombre_sub', 'caracteristica'))

    nombre_sub = models.CharField(max_length=100)
    caracteristica = models.ForeignKey(
        CaracteristicaMedio, on_delete=models.CASCADE)
    atributo = models.TextField()
    comentario = models.TextField()

    def get_model_type(self): # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "SubaracteristicaMedio"

class TipoCosto(models.Model):
    """ Tabla para almacenar la informacion del tipo de costo de un proyecto.
    Parametros:
        models.Model (TipoCosto): Instancia sobre la que se crea la tabla.
    Atributos:
        tipo: Tipo de costo
    """
    TYPE_CHOICES = (('humano', 'Talento Humano'),
                    ('profesionales', 'Servicios Profesionales y Técnicos'),
                    ('hospedaje', 'Pasajes y Hospedaje'),
                    ('materiales', 'Recursos Materiales'),
                    ('oficina', 'Materiales de Oficina'),
                    ('insumos', 'Insumos'))
    tipo = models.CharField(max_length=100, choices=TYPE_CHOICES, unique=True)

    def get_model_type(self): # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "TipoCosto"
    def __str__(self): # pylint: disable=no-self-use
        '''Devuelve el modelo en tipo String'''
        return self.tipo


class CostoHumano(models.Model):
    """ Tabla para almacenar los detalles de los costos humanos de un proyecto.
    Parametros:
        models.Model (CostoHumano): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: Proyecto asociado
        tipo: Tipo de costo
        actividad: Descripcion de la actividad realizada
        cantidad: Cantidad de personas o equipos requeridos
        tiempo: Lapso durante el cual se realizó la actividad
        monto: Monto total de la actividad
    """
    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoCosto, on_delete=models.PROTECT)
    actividad = models.TextField()
    cantidad = models.TextField()
    tiempo = models.CharField(max_length=100)
    monto = models.FloatField(validators=[MinValueValidator(0)])

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "CostoHumano"


class CostoMateriales(models.Model):
    """ Tabla para almacenar los detalles de los costos de materiales de un proyecto.
    Parametros:
        models.Model (CostoMateriales): Instancia sobre la que se crea la tabla.
    Atributos:
        proyecto: Proyecto asociado
        tipo: Tipo de costo
        material: Materiales utilizados
        cantidad: Cantidad de materiales utilizados
        costo_unidad: Costo por unidad de los materiales
        monto: Monto total de los materiales
    """
    proyecto = models.ForeignKey(DatosProyecto, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoCosto, on_delete=models.PROTECT)
    material = models.CharField(max_length=100)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    costo_unidad = models.FloatField(validators=[MinValueValidator(0)])
    monto = models.FloatField(validators=[MinValueValidator(0)])

    def get_model_type(self):  # pylint: disable=no-self-use
        '''Devuelve el tipo de modelo'''
        return "CostoMateriales"
