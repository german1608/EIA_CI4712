'''
    Clase que representa la tabla de los usuarios del sistema
'''
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    '''
        Esta clase representa a los usuarios que van a estar dentro del
        sistema
    '''
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'doc_identidad']

    def __str__(self):
        return self.email

    def full_name(self):
        """ Retorna el nombre completo del usuario """
        return '{} {}'.format(self.first_name, self.last_name)
