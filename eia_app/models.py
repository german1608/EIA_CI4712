"""
    Archivo con todos los modelos necesarios
    para la creacion de un EsIA.
"""

import datetime
import re
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Datos_Persona(models.Model):
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
    class Meta:
        unique_together = (('cedula', 'pasaporte'))
    nombre = models.CharField(
        max_length = 60, 
        validators = [RegexValidator(re.compile('^[\w+\s]+$'),
        _('Nombre incorrecto'), 'invalid')]
    )
    apellido = models.CharField(
        max_length = 60, 
        validators = [RegexValidator(re.compile('^[\w+\s]+$'),
        _('Apellido incorrecto'), 'invalid')]
    )
    cedula = models.CharField(
        max_length = 8,
        validators = [RegexValidator(re.compile('/^[V|E|J|P][0-9]{5,9}$/'),
        _('Cédula incorrecta'), 'invalid')]
    )
    pasaporte = models.IntegerField(
        validators = [MinValueValidator(0)]
    )

class Organizacion(models.Model):
    """ Tabla de las organizaciones que proponen un proyecto
    al EsIA.
    Parametros:
        models.Model (Organizacion): Instancia sobre la que se
        crea la tabla.
    Atributos de la clase:
        razon_social: Razon social de la organizacion
        nombre: Nombre de la orgnizacion
        rif: Rif de la organizacion
        direccion: direccion de la organizacion
        representante_legal: Datos del representante legal de la organizacion
        telefono: Telefono de la organizacion
        email: Email de la organizacion
    """
    RAZON_SOCIAL_CHOICES = (
        ('natural', 'Persona natural'),
        ('juridica', 'Persona Jurídica')
    )
    razon_social = models.CharField(
        max_length = 8,
        choices = RAZON_SOCIAL_CHOICES,    
    )
    nombre = models.CharField(
        max_length = 100
    )
    rif = models.CharField(
        max_length = 12,
        unique = True,
        validators = [RegexValidator(re.compile('^([VEJPGvejpg]{1})-([0-9]{8})-([0-9]{1}$)'),
        _('RIF incorrecto'), 'invalid')]
    )
    direccion = models.TextField()
    nombre_representante_legal = models.CharField(
        max_length = 60, 
        validators = [RegexValidator(re.compile('^[\w+\s]+$'),
        _('Nombre incorrecto'), 'invalid')]
    )
    apellido_representante_legal = models.CharField(
        max_length = 60, 
        validators = [RegexValidator(re.compile('^[\w+\s]+$'),
        _('Apellido incorrecto'), 'invalid')]
    )
    cedula_representante_legal = models.CharField(
        max_length = 9,
        validators = [RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'),
        _('Cédula incorrecta'), 'invalid')]
    )
    pasaporte_representante_legal = models.IntegerField(
        validators = [MinValueValidator(0)],
        blank = True,
        null =  True
    )
    telefono = models.CharField(
        max_length = 11,
        validators = [RegexValidator((re.compile('^[0-9]{11}$')), 
        _('Teléfono incorrecto'), 'invalid')]
    )
    email = models.EmailField()
    

class Solicitante(models.Model):
    """ Tabla que referencia a los datos de una persona
    para almacenar los datos de un solicitante o promotor del proyecto.
    Parametros:
        models.Model (Solicitante): Instancia sobre la que se crea la tabla.
    Atributos:
        solicitante: Datos personales del solicitante o promotor.
    """
    solicitante = models.ForeignKey(
        Datos_Persona, 
        on_delete=models.CASCADE
    )

class Responsable(models.Model):
    """ Tabla que referencia a los datos de una persona
    para almacenar los datos de responsable de un proyecto.
    Parametros:
        models.Model (Solicitante): Instancia sobre la que se crea la tabla.
    Atributos:
        responsable: Datos personales del responsable del proyecto.
    """
    responsable = models.ForeignKey(
        Datos_Persona,
        on_delete = models.CASCADE
    )

class Datos_Proyecto(models.Model):
    """ Tabla para almacenar la informacion general de un proyecto.
    Parametros:
        models.Model (Datos_Proyecto): Instancia sobre la que se crea la tabla.
    Atributos:
        titulo: Titulo del proyecto
        ubicacion: ubicacion geografica donde se desarrollara el proyecto
        area: area de desempeño del proyecto
        tipo: tipo de proyecto
        url: Url al PDF del proyecto.
    """
    titulo = models.CharField(
        max_length = 100,
        primary_key = True
    )
    ubicacion = models.TextField()
    area = models.TextField()
    tipo = models.TextField()
    url = models.URLField()