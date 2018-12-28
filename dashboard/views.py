"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import DatosProyectoSerializer
from eia_app.models import DatosProyecto
from rest_framework import viewsets

# Create your views here.

class DashboardViewSet(viewsets.ModelViewSet):
    """
    Produce la vista con el json que contiene la informacion
    para que el dashboard la muestre
    """
    queryset = DatosProyecto.objects.all()
    serializer_class = DatosProyectoSerializer

class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
