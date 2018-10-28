from django.urls import path, re_path
from .views import *

app_name = 'eia_app'

urlpatterns = [
    path('organizaciones/', OrganizacionList.as_view(), name='lista-organizaciones'),
    path('organizaciones/nuevo/', OrganizacionCreate.as_view(), name='nueva-organizacion'),
    re_path(r'^organizaciones/(?P<pk>\d+)/$', OrganizacionDetail.as_view(), name='detalles-organizacion'),
    re_path(r'^organizaciones/editar/(?P<pk>\d+)/$', OrganizacionUpdate.as_view(), name='editar-organizacion'),
    re_path(r'^organizaciones/borrar/(?P<pk>\d+)/$', OrganizacionDelete.as_view(), name='borrar-organizacion'),
    path('datos_proyectos/', Datos_ProyectoList.as_view(), name='lista-datos-proyectos'),
    path('datos_proyectos/nuevo/', Datos_ProyectoCreate.as_view(), name='nueva-datos-proyecto'),
    re_path(r'^datos_proyectos/(?P<pk>\d+)/$', Datos_ProyectoDetail.as_view(), name='detalles-datos-proyecto'),
    re_path(r'^datos_proyectos/editar/(?P<pk>\d+)/$', Datos_ProyectoUpdate.as_view(), name='editar-datos-proyecto'),
    re_path(r'^datos_proyectos/borrar/(?P<pk>\d+)/$', Datos_ProyectoDelete.as_view(), name='borrar-datos-proyecto'),
]
