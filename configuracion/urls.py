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
from configuracion.views import EstudioUpdate, EstudioCreate 
from configuracion.views import ActividadCreate, ActividadUpdate, ActividadDelete
from configuracion.views import DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete
from configuracion.views import MacroCreate, MacroUpdate, MacroDelete
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('agregar_estudio/', EstudioCreate.as_view(), name='agregar_estudio'),
    path('editar_estudio/<int:pk>/', EstudioUpdate.as_view(), name='editar_estudio'),
    path('eliminar_estudio/<int:pk_id>/', views.eliminar_estudio, name='eliminar_estudio'),
    path('tablas/', views.tablas, name='tablas'),
    path('modificar_tablas/', views.modificar_tablas, name='modificar_tablas'),
    path('agregar_actividad/', ActividadCreate.as_view(), name='agregar_actividad'),
    path('editar_actividad/<int:pk>/', ActividadUpdate.as_view(), name='editar_actividad'),
    path('eliminar_actividad/<int:pk_id>/', ActividadDelete.as_view(), name='eliminar_actividad'),
    path('agregar_disciplina/', DisciplinaCreate.as_view(), name='agregar_disciplina'),
    path('editar_disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='editar_disciplina'),
    path('eliminar_disciplina/<int:pk_id>/', DisciplinaDelete.as_view(), name='eliminar_disciplina'),
    path('agregar_macro/', MacroCreate.as_view(), name='agregar_macro'),
    path('editar_macro/<int:pk>/', MacroUpdate.as_view(), name='editar_macro'),
    path('eliminar_macro/<int:pk_id>/', MacroDelete.as_view(), name='eliminar_macro'),
    path('actividades/', views.actividades, name='actividades'),
]
