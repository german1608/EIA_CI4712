'''
    Modulo donde se implementan los formularios para la creacion
    de nuevos usuarios para el sistema. Esto se puede llevar
    al front
'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import Group

from .models import Usuario
#pylint: disable=r0903
class CustomUserCreationForm(UserCreationForm):
    '''
        Aqui se implementa el formulario para la creacion
        de nuevos usuarios del sistema
    '''
    rol = forms.ModelChoiceField(queryset=Group.objects.all(), label='Rol')
    class Meta(UserCreationForm.Meta):
        '''
            Aqui se especifica que datos se tienen que incluir en
            el formulario
        '''
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'doc_identidad', 'username')

    def save(self, commit=True):
        instance = super().save(commit)
        rol = self.cleaned_data['rol']
        instance.groups.set([rol])
        return instance

class CustomUserChangeForm(UserChangeForm):
    '''
        Clase que implementa el formulario para la actualizacion
        de los datos de un usuario que ya existe en el sistema
    '''
    rol = forms.ModelChoiceField(queryset=Group.objects.all(), label='Rol')
    class Meta(UserChangeForm.Meta):
        '''
            Aqui se especifica que datos son los que se pueden modificar
        '''
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')

    def save(self, commit=True):
        instance = super().save(commit)
        rol = self.cleaned_data['rol']
        instance.groups.set([rol])
        return instance
