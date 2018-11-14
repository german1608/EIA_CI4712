"""configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from configuracion.views import EstudioUpdate, EstudioCreate, ActividadCreate
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('agregar_estudio/', EstudioCreate.as_view(), name='agregar_estudio'),
    path('editar_estudio/<int:pk>/', EstudioUpdate.as_view(), name='editar_estudio'),
    path('eliminar_estudio/<int:pk_id>/', views.eliminar_estudio, name='eliminar_estudio'),
    path('tablas/', views.tablas, name='tablas'),
    path('modificar_tablas/', views.modificar_tablas, name='modificar_tablas'),
    path('agregar_actividad/', ActividadCreate.as_view(), name='agregar_actividad'),
]
