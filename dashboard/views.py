"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from eia_app.models import DatosProyecto
from .serializers import DatosProyectoSerializer

# Create your views here.

class DashboardViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """
    Produce la vista con el json que contiene la informacion
    para que el dashboard la muestre
    """
    queryset = DatosProyecto.objects.all()
    serializer_class = DatosProyectoSerializer

class DashboardView(LoginRequiredMixin, TemplateView):# pylint: disable=too-many-ancestors
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
