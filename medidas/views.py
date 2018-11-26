'''Views del crud del consultor'''

from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import (
    Medida
)
from .forms import (
    MedidaCreateForm
)

class MedidaList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las medidas'''
    model = Medida
    template_name =  'medidas/list.html'

class MedidaCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Medida
    form_class = MedidaCreateForm
    template_name = 'medidas/create_form.html'
    success_url = reverse_lazy('medidas:lista-medidas')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedidaCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Medida"
        return context

class MedidaDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una medida'''
    model = Medida
    template_name = 'medidas/detail.html'

class MedidaUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una medida'''
    model = Medida
    template_name = 'medidas/create_form.html'
    success_url = reverse_lazy('medidas:lista-medidas')
    fields = '__all__'

class MedidaDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una medida'''
    model = Medida
    template_name = 'medidas/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')