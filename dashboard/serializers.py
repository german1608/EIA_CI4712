"""
    Script que se encarga de transformar la informacion
    necesaria en un json para poder mostrar en el
    front-end
"""
from rest_framework import serializers
from eia_app.models import DatosProyecto

class DatosProyectoSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Clase que se encarga de producir el json con la informacion
    de los proyectos. Aqui se especifica que campos se necesitan
    '''
    class Meta:
        model = DatosProyecto
        fields = ('pk', 'titulo')
