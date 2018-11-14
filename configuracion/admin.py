"""Admin de los modelos
"""
from django.contrib import admin
from configuracion.models import Estudio, Intensidad, Extension, Duracion, Reversibilidad
from configuracion.models import Probabilidad, Importancia, Macro, Disciplina, Actividad
# Register your models here.

admin.site.register(Estudio)
admin.site.register(Intensidad)
admin.site.register(Extension)
admin.site.register(Duracion)
admin.site.register(Reversibilidad)
admin.site.register(Probabilidad)
admin.site.register(Importancia)
admin.site.register(Macro)
admin.site.register(Disciplina)
admin.site.register(Actividad)
