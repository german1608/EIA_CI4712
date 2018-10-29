'''Modulo de urls del crud del consultor '''

from django.urls import path, re_path
from .views import * #pylint: disable=wildcard-import, unused-wildcard-import

app_name = 'eia_app' #pylint: disable=invalid-name

urlpatterns = [ #pylint: disable=invalid-name
    path('organizaciones/', OrganizacionList.as_view(),
         name='lista-organizaciones'),
    path('organizaciones/nuevo/', OrganizacionCreate.as_view(),
         name='nueva-organizacion'),
    re_path(r'^organizaciones/(?P<pk>\d+)/$', OrganizacionDetail.as_view(),
            name='detalles-organizacion'),
    re_path(r'^organizaciones/editar/(?P<pk>\d+)/$', OrganizacionUpdate.as_view(),
            name='editar-organizacion'),
    re_path(r'^organizaciones/borrar/(?P<pk>\d+)/$', OrganizacionDelete.as_view(),
            name='borrar-organizacion'),
    path('datos_proyectos/', DatosProyectoList.as_view(),
         name='lista-datos-proyectos'),
    path('datos_proyectos/nuevo/', DatosProyectoCreate.as_view(),
         name='nueva-datos-proyecto'),
    re_path(r'^datos_proyectos/(?P<pk>\d+)/$', DatosProyectoDetail.as_view(),
            name='detalles-datos-proyecto'),
    re_path(r'^datos_proyectos/editar/(?P<pk>\d+)/$', DatosProyectoUpdate.as_view(),
            name='editar-datos-proyecto'),
    re_path(r'^datos_proyectos/borrar/(?P<pk>\d+)/$', DatosProyectoDelete.as_view(),
            name='borrar-datos-proyecto'),
    path('responsables/', ResponsableList.as_view(),
         name='lista-responsables'),
    path('responsables/nuevo/', ResponsableCreate.as_view(),
         name='nuevo-responsable'),
    re_path(r'^responsables/(?P<pk>\d+)/$', ResponsableDetail.as_view(),
            name='detalles-responsable'),
    re_path(r'^responsables/editar/(?P<pk>\d+)/$', ResponsableUpdate.as_view(),
            name='editar-responsable'),
    re_path(r'^responsables/borrar/(?P<pk>\d+)/$', ResponsableDelete.as_view(),
            name='borrar-responsable'),
]
