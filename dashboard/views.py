"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView

# Create your views here.

class DashboardView(TemplateView):
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
