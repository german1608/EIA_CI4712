"""
Modelos para el modulo de medidas
"""
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Medida(models.Model):
    """
    Declaracion de modelo de Medidas de eia.
    """
    nomenclatura = models.CharField(max_length=10, unique=True, verbose_name='Nomenclatura')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    TIPO_CORRECTIVA = 0
    TIPO_CHOICES = (
        (TIPO_CORRECTIVA, 'Correctiva'),
    )
    tipo = models.IntegerField(choices=TIPO_CHOICES, verbose_name='Tipo')
    MEDIO_FISICO = 0
    MEDIO_BIOLOGICO = 1
    MEDIO_SOCIO_CULTURAL = 2
    MEDIO_CHOICES = (
        (MEDIO_FISICO, 'Físico'),
        (MEDIO_BIOLOGICO, 'Biológico'),
        (MEDIO_SOCIO_CULTURAL, 'Socio-Cultural')
    )
    medio = models.IntegerField(choices=MEDIO_CHOICES, verbose_name='Medio')
    descripcion = models.TextField(verbose_name='Descripción')
    marco_juridico = models.TextField(verbose_name='Marco Jurídico')
    area = models.TextField(verbose_name='Área')
    nombre_responsable = models.CharField(max_length=100, verbose_name='Nombre del Responsable')
    apellido_responsable = models.CharField(max_length=100, verbose_name='Apellido del Responsable')
    nivel_academico_responsable = models.DecimalField(
        verbose_name='Nivel Académico del Responsable',
        max_digits=5,
        decimal_places=4)
    ci_responsable = models.CharField(
        max_length=10, verbose_name='Cédula del Responsable',
        validators=[RegexValidator(
            r'/^[V|E|J|P][0-9]{5,9}$/',
            'Cédula incorrecta',
            'invalid')])

class Impacto(models.Model):
    """ Tabla de Impactos que sirve de atributo multivalor para las medidas """
    medida = models.ForeignKey(Medida, related_name='impactos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')

class Objetivo(models.Model):
    """ Tabla de Objetivos que sirve de atributo multivalor para las medidas """
    medida = models.ForeignKey(
        Medida, related_name='objetivos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')

class IndicadorDeCumplimiento(models.Model):
    """
    Tabla de Indicador De Cumplimientos que sirve de atributo multivalor para las medidas
    """
    medida = models.ForeignKey(
        Medida, related_name='indicadoresdecumplimientos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
