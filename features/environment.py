'''
Declaracion de entorno de behave
'''
from selenium import webdriver

def before_all(context):
    ''' Funcion que se ejecuta antes de cada prueba de behave '''
    context.browser = webdriver.Firefox()

def after_all(context):
    ''' Funcion que se ejecuta luego de ejecutar todas las pruebas de los .feature '''
    context.browser.quit()
