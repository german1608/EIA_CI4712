"""
    Script que se encarga de transformar la informacion
    necesaria en un json para poder mostrar en el
    front-end
"""
from rest_framework import serializers
from eia_app.models import DatosProyecto
from users.models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Clase que se encarga de producir el json con la informacion
    de un usuario
    '''
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name')

class DatosProyectoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Clase que se encarga de producir el json con la informacion
    de los proyectos. Aqui se especifica que campos se necesitan
    '''
    class Meta:
        model = DatosProyecto
        fields = ('pk', 'titulo')
