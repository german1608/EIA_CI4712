"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
