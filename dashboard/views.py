"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.response import Response
from eia_app.models import DatosProyecto
from users.models import Usuario
from .serializers import DatosProyectoSerializer, UsuarioSerializer

# Create your views here.

class ProyectosViewSet(viewsets.ViewSet): # pylint: disable=too-many-ancestors
    """
    Produce la vista con el json que contiene la informacion
    para que el dashboard la muestre
    """
    def list(self, request): # pylint: disable=no-self-use
        '''
        Devuelve un json con solo los proyectos del
        usuario loggeado
        '''
        usuario_loggeado = request.user
        queryset = DatosProyecto.objects.filter(usuario=usuario_loggeado)
        serializer = DatosProyectoSerializer(queryset, many=True)

        # Aqui se manda al contexto, ademas de los proyectos el usuario loggeado
        queryset_usuario = Usuario.objects.filter(pk=usuario_loggeado.pk)
        serializer_usuario = UsuarioSerializer(queryset_usuario, many=True)
        return Response({'usuario': serializer_usuario.data, 'proyectos': serializer.data})
        # return Response(serializer.data)

class DashboardView(LoginRequiredMixin, TemplateView):# pylint: disable=too-many-ancestors
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
