from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


'''
    Clase que implementa el formulario para la creacion 
    de nuevos usuarios para el sistema. Esto se puede llevar 
    al front 
'''
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('nombre', 'apellido', 'correo', 'clave', 'doc_identidad')

'''
    Clase que implementa el formulario para la actualizacion 
    de los datos de un usuario que ya existe en el sistema 
'''

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'correo', 'clave', 'doc_identidad')