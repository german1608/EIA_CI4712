from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('nombre', 'apellido', 'correo', 'clave', 'doc_identidad')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'correo', 'clave', 'doc_identidad')