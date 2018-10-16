from django.db import models

# Create your models here.
# Aqui se crea el modelo de usuarios. Es la tabla que contenera 
# los datos de los usuarios del sistema 

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    # Esta clave debe tener una funcion que la encripta 
    # En este field realmente se va almacenar la clave encriptada 
    clave = models.CharField(max_length=200)
    doc_identidad = models.PositiveIntegerField()