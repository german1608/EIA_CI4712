"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import ensure_csrf_cookie
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
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

# @ensure_csrf_cookie
class DashboardView(LoginRequiredMixin, TemplateView):# pylint: disable=too-many-ancestors
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
    success_url = reverse_lazy('consultor-crud-index')
    def post(self, request, *args, **kwargs):
        habilitar_edicion = dict(request.POST)
        proyecto_pk = habilitar_edicion["edicion_habilitada"][0]
        proyecto = DatosProyecto.objects.get(pk=proyecto_pk)
        proyecto.edicion_habilitada = True
        proyecto.save()
        return HttpResponse(self.success_url)