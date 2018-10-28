'''
    Este archivo lo que sirve es para poder incluir
    configuraciones para la app de users
'''
from django.apps import AppConfig


class UsersConfig(AppConfig):
    '''
        Aqui se crea una configuracion para los usuarios del
        sistema
    '''
    name = 'users'
