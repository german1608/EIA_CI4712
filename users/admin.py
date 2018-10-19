'''
    En este archivo estan las configuraciones para el admin
    de la aplicacion web
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Formularios
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario

# Register your models here.

class CustomUserAdmin(UserAdmin):
    '''
        Aqui se establece la conexion entre el modelo
        y la pagina admin de la aplicacion web
    '''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['email']

admin.site.register(Usuario, CustomUserAdmin)
