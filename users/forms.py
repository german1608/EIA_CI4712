'''
    Modulo donde se implementan los formularios para la creacion
    de nuevos usuarios para el sistema. Esto se puede llevar
    al front
'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import Usuario
#pylint: disable=r0903
class CustomUserCreationForm(UserCreationForm):
    '''
        Aqui se implementa el formulario para la creacion
        de nuevos usuarios del sistema
    '''
    class Meta(UserCreationForm.Meta):
        '''
            Aqui se especifica que datos se tienen que incluir en
            el formulario
        '''
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')
        labels = {
            'doc_identidad': _('Documento Identidad')
        }

class CustomUserChangeForm(UserChangeForm):
    '''
        Clase que implementa el formulario para la actualizacion
        de los datos de un usuario que ya existe en el sistema
    '''
    class Meta:
        '''
            Aqui se especifica que datos son los que se pueden modificar
        '''
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')
