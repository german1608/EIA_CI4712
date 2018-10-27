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

class OrganizacionDetail(DetailView):
    model = Organizacion

class OrganizacionCreate(CreateView):
    model = Organizacion
    form_class = OrganizacionCreateForm
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

class OrganizacionUpdate(UpdateView):
    model = Organizacion
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'

class OrganizacionDelete(DeleteView):
    model = Organizacion
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

def ConsultorIndex(request):
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)