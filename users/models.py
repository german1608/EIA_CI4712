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
    correo = models.EmailField(unique=True)
    # Esta clave debe tener una funcion que la encripta
    # En este field realmente se va almacenar la clave encriptada
    doc_identidad = models.PositiveIntegerField()

    def __str__(self):
        return self.correo
