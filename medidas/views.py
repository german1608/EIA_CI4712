'''Views del crud del consultor'''

from django.shortcuts import render, redirect
from django.db import transaction
from django.views.generic import (CreateView, DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import (
    Medida
)
from .forms import (
    MedidaForm, ImpactoFormSet, ObjetivoFormSet, IndicadorDeCumplimientoFormSet
)

class MedidaList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las medidas'''
    model = Medida
    template_name = 'medidas/list.html'

class MedidaCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Medida
    form_class = MedidaForm
    template_name = 'medidas/form.html'
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
    template_name = 'medidas/form.html'
    success_url = reverse_lazy('medidas:lista-medidas')
    form_class = MedidaForm

class MedidaDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una medida'''
    model = Medida
    template_name = 'medidas/delete.html'
    success_url = reverse_lazy('medidas:lista-medidas')

@transaction.atomic
def medida_form_view(request, pk=None):
    """
    Vista que maneja la creacion de medidas tomando en cuenta
    las relaciones de sus tablas multivalores. El uso de transaction.atomic
    es para evitar crear un objeto sin crear los dependientes.
    """
    try:
        medida = Medida.objects.get(pk=pk)
    except Medida.DoesNotExist:
        medida = Medida()

    medida_form = MedidaForm(instance=medida)
    impacto_formset = ImpactoFormSet(instance=medida)
    objetivo_formset = ObjetivoFormSet(instance=medida)
    indicador_formset = IndicadorDeCumplimientoFormSet(instance=medida)
    if request.method == 'POST':
        medida_form = MedidaForm(request.POST, instance=medida)
        if medida_form.is_valid():
            medida_form.save()
            impacto_formset = ImpactoFormSet(request.POST, instance=medida)
            objetivo_formset = ObjetivoFormSet(request.POST, instance=medida)
            indicador_formset = IndicadorDeCumplimientoFormSet(request.POST, instance=medida)

            if impacto_formset.is_valid() and objetivo_formset.is_valid() and\
                indicador_formset.is_valid():
                impacto_formset.save()
                objetivo_formset.save()
                indicador_formset.save()
                return redirect('medidas:lista-medidas')
            print(impacto_formset.errors)
            print(objetivo_formset.errors)
            print(indicador_formset.errors)
    return render(request, 'medidas/form.html', {
        'medida_form': medida_form,
        'impacto_formset': impacto_formset,
        'objetivo_formset': objetivo_formset,
        'indicador_formset': indicador_formset,
    })
