"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # Obtengo el usuario que esta loggeado en el momento
        usuario_loggeado = self.request.user
        # Obtengo los proyectos asociados a ese usuario
        lista_proyectos = usuario_loggeado.datosproyecto_set.all()
        context['proyectos'] = lista_proyectos
        context['usuario'] = usuario_loggeado
        # Si existe un proyecto seleccionado agregarlo al contexto
        if usuario_loggeado.proyecto_seleccionado > 0:
            editable = lista_proyectos.get(pk=(usuario_loggeado.proyecto_seleccionado))
            context['edicion'] = editable
        return context

    def get(self, request, *args, **kwargs):
        '''
        Metodo que se encarga de manejar los request tipo GET
        a la vista de seleccion de un proyecto
        '''
        usuario_loggeado = self.request.user
        usuario_loggeado.proyecto_seleccionado = -1
        usuario_loggeado.save()
        return super().get(request)

    def post(self, request, *args, **kwargs):
        '''
        Metodo que se encarga de manejar el request tipo POST
        hecho desde la vista para la seleccion de un proyecto
        a editar
        '''
        # Agrega la pk del proyecto seleccionado para editar
        # por el usuario
        usuario_loggeado = self.request.user
        usuario_loggeado.proyecto_seleccionado = request.POST.get('proyecto')
        usuario_loggeado.save()
        return HttpResponseRedirect(reverse_lazy('eia_app:consultor-crud-index'))
