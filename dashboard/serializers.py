"""
    Script que se encarga de transformar la informacion
    necesaria en un json para poder mostrar en el 
    front-end
"""
from eia_app.models import DatosProyecto
from rest_framework import serializers

class DatosProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatosProyecto
        fields = ('pk', 'titulo')