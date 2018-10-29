'''Views del crud del consultor'''

from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import * #pylint: disable=wildcard-import, unused-wildcard-import
from .forms import * #pylint: disable=wildcard-import, unused-wildcard-import


class OrganizacionList(ListView): # pylint: disable=too-many-ancestors
    '''Listar las organizaciones'''
    model = Organizacion
    template_name = 'eia_app/crud_list.html'

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(OrganizacionList, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context


class OrganizacionDetail(DetailView): # pylint: disable=too-many-ancestors
    '''Detalles de una organizacion'''
    model = Organizacion
    template_name = 'eia_app/crud_detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrganizacionDetail, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context


class OrganizacionCreate(CreateView): # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Organizacion
    form_class = OrganizacionCreateForm
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(OrganizacionCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Organización"
        return context


class OrganizacionUpdate(UpdateView): # pylint: disable=too-many-ancestors
    '''Actualizar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'


class OrganizacionDelete(DeleteView): # pylint: disable=too-many-ancestors
    '''Eliminar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/crud_confirm_delete.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

    def get_context_data(self, **kwargs):
        context = super(OrganizacionDelete, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context


class DatosProyectoList(ListView): # pylint: disable=too-many-ancestors
    '''Listar los datos de los proyectos'''
    model = DatosProyecto
    template_name = 'eia_app/crud_list.html'

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(DatosProyectoList, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context


class DatosProyectoCreate(CreateView): # pylint: disable=too-many-ancestors
    '''Crear datos de un proyecto'''
    model = DatosProyecto
    fields = '__all__'
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(DatosProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Datos de un proyecto"
        return context


class DatosProyectoUpdate(UpdateView): # pylint: disable=too-many-ancestors
    '''Actualizar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    fields = '__all__'


class DatosProyectoDelete(DeleteView): # pylint: disable=too-many-ancestors
    '''Eliminar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/crud_confirm_delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

    def get_context_data(self, **kwargs):
        context = super(DatosProyectoDelete, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context


class DatosProyectoDetail(DetailView): # pylint: disable=too-many-ancestors
    '''Detalles de los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/crud_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DatosProyectoDetail, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context

class ResponsableList(ListView): # pylint: disable=too-many-ancestors
    '''Listar las Responsables'''
    model = Responsable
    template_name = 'eia_app/crud_list.html'

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(ResponsableList, self).get_context_data(**kwargs)
        context["Responsable"] = True
        return context


class ResponsableDetail(DetailView): # pylint: disable=too-many-ancestors
    '''Detalles de una Responsable'''
    model = Responsable
    template_name = 'eia_app/crud_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ResponsableDetail, self).get_context_data(**kwargs)
        context["Responsable"] = True
        return context


class ResponsableCreate(CreateView): # pylint: disable=too-many-ancestors
    '''Crear una Responsable'''
    model = Responsable
    form_class = ResponsableCreateForm
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')

    def get_context_data(self, **kwargs): #pylint: disable=arguments-differ
        context = super(ResponsableCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Responsable"
        return context


class ResponsableUpdate(UpdateView): # pylint: disable=too-many-ancestors
    '''Actualizar una Responsable'''
    model = Responsable
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    fields = '__all__'


class ResponsableDelete(DeleteView): # pylint: disable=too-many-ancestors
    '''Eliminar una Responsable'''
    model = Responsable
    template_name = 'eia_app/crud_confirm_delete.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')

    def get_context_data(self, **kwargs):
        context = super(ResponsableDelete, self).get_context_data(**kwargs)
        context["Responsable"] = True
        return context


def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)
