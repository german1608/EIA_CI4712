from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
) 
from .models import *
from django.urls import reverse_lazy
from .forms import *

class OrganizacionList(ListView):
    model = Organizacion
    template_name = 'eia_app/crud_list.html'
    def get_context_data(self, **kwargs):
        context = super(OrganizacionList, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context

class OrganizacionDetail(DetailView):
    model = Organizacion
    template_name = 'eia_app/crud_detail.html'
    def get_context_data(self, **kwargs):
        context = super(OrganizacionDetail, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context

class OrganizacionCreate(CreateView):
    model = Organizacion
    form_class = OrganizacionCreateForm
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

class OrganizacionUpdate(UpdateView):
    model = Organizacion
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'

class OrganizacionDelete(DeleteView):
    model = Organizacion
    template_name = 'eia_app/crud_confirm_delete.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    def get_context_data(self, **kwargs):
        context = super(OrganizacionDelete, self).get_context_data(**kwargs)
        context["Organizacion"] = True
        return context

class Datos_ProyectoList(ListView):
    model = Datos_Proyecto
    template_name = 'eia_app/crud_list.html'
    def get_context_data(self, **kwargs):
        context = super(Datos_ProyectoList, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context

class Datos_ProyectoCreate(CreateView):
    model = Datos_Proyecto
    fields = '__all__'
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

class Datos_ProyectoUpdate(UpdateView):
    model = Datos_Proyecto
    template_name = 'eia_app/crud_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    fields = '__all__'

class Datos_ProyectoDelete(DeleteView):
    model = Datos_Proyecto
    template_name = 'eia_app/crud_confirm_delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    def get_context_data(self, **kwargs):
        context = super(Datos_ProyectoDelete, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context

class Datos_ProyectoDetail(DetailView):
    model = Datos_Proyecto
    template_name = 'eia_app/crud_detail.html'
    def get_context_data(self, **kwargs):
        context = super(Datos_ProyectoDetail, self).get_context_data(**kwargs)
        context["Datos_Proyecto"] = True
        return context


def ConsultorIndex(request):
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)