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
    doc_identidad = models.CharField(max_length=10)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'doc_identidad']

    def __str__(self):
        return self.email
