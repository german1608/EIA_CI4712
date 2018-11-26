'''Modulo de urls de las medidas '''

from django.urls import path, re_path
from .views import * #pylint: disable=wildcard-import, unused-wildcard-import

app_name = 'medidas' #pylint: disable=invalid-name

urlpatterns = [ #pylint: disable=invalid-name
    path('medidas/', MedidaList.as_view(),
         name='lista-medidas'),
    path('medidas/nuevo/', MedidaCreate.as_view(),
         name='nueva-medida'),
    re_path(r'^medidas/editar/(?P<pk>\d+)/$', MedidaUpdate.as_view(),
            name='editar-medida'),
    re_path(r'^medidas/(?P<pk>\d+)/$', MedidaDetail.as_view(),
            name='detalles-medida'),
    re_path(r'^medidas/borrar/(?P<pk>\d+)/$', MedidaDelete.as_view(),
            name='borrar-medida'),
]
