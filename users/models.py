'''
    Clase que representa la tabla de los usuarios del sistema
'''
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class Usuario(AbstractUser):
    '''
        Esta clase representa a los usuarios que van a estar dentro del
        sistema
    '''
    doc_identidad = models.CharField(max_length=10,
                                     validators=[RegexValidator(r'^[VEF]-\d+$',
                                                                'Formato de documento de identidad'
                                                                ' inválido. Los números deben '
                                                                'estar precedidos por V- o E-.'
                                                                )],
                                     verbose_name='Documento de Identidad',
                                     unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField('Dirección de correo electrónico', blank=True, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'doc_identidad']

    @property
    def rol(self):
        """ Obtiene el rol del usuario """
        return self.groups.all().first()

    def __str__(self):
        return self.email

    def full_name(self):
        """ Retorna el nombre completo del usuario """
        return '{} {}'.format(self.first_name, self.last_name)
