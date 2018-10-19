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
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    doc_identidad = models.PositiveIntegerField()
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email', 'doc_identidad']

    def __str__(self):
        return self.email
