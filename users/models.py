from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
    Clase que representa la tabla de los usuarios del sistema 
'''

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    # Esta clave debe tener una funcion que la encripta 
    # En este field realmente se va almacenar la clave encriptada 
    clave = models.CharField(max_length=200)
    doc_identidad = models.PositiveIntegerField()

    def __str__(self):
        return self.correo