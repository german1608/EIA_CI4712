'''Modulo de urls de las medidas '''

from django.urls import path, re_path
from .views import (
    MedidaListView, MedidaDetail, MedidaDelete, medida_form_view
)

app_name = 'medidas' #pylint: disable=invalid-name

urlpatterns = [ #pylint: disable=invalid-name
    path('', MedidaListView.as_view(),
         name='lista-medidas'),
    path('nuevo/', medida_form_view,
         name='nueva-medida'),
    re_path(r'^editar/(?P<pk>\d+)/$', medida_form_view,
            name='editar-medida'),
    re_path(r'^(?P<pk>\d+)/$', MedidaDetail.as_view(),
            name='detalles-medida'),
    re_path(r'^borrar/(?P<pk>\d+)/$', MedidaDelete.as_view(),
            name='borrar-medida'),
]
