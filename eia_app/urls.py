from django.urls import path, re_path
from .views import *

app_name = 'eia_app'

urlpatterns = [
    path('organizaciones/', OrganizacionList.as_view(), name='lista-organizaciones'),
    path('organizaciones/nuevo/', OrganizacionCreate.as_view(), name='nueva-organizacion'),
    re_path(r'^organizaciones/(?P<pk>\d+)/$', OrganizacionDetail.as_view(), name='detalles-organizacion'),
    re_path(r'^organizaciones/editar/(?P<pk>\d+)/$', OrganizacionUpdate.as_view(), name='editar-organizacion'),
    re_path(r'^organizaciones/borrar/(?P<pk>\d+)/$', OrganizacionDelete.as_view(), name='borrar-organizacion'),
]
