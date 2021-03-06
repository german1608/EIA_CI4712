'''Views del crud del consultor'''

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.views.generic import (DetailView,
                                  ListView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import (
    Medida
)
from .forms import (
    MedidaForm, ImpactoFormSet, ObjetivoFormSet, IndicadorDeCumplimientoFormSet
)

class MedidaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las medidas'''
    model = Medida
    template_name = 'medidas/list.html'
    permission_required = ('medidas.view_medida',
                           'medidas.view_impacto', 'medidas.view_objetivo',
                           'medidas.view_indicadordecumplimiento')

class MedidaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una medida'''
    model = Medida
    template_name = 'medidas/detail.html'
    permission_required = ('medidas.view_medida',
                           'medidas.view_impacto', 'medidas.view_objetivo',
                           'medidas.view_indicadordecumplimiento')


class MedidaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una medida'''
    model = Medida
    template_name = 'medidas/delete.html'
    success_url = reverse_lazy('medidas:lista-medidas')
    permission_required = ('medidas.delete_medida',
                           'medidas.delete_impacto', 'medidas.delete_objetivo',
                           'medidas.delete_indicadordecumplimiento')

@login_required
@permission_required(('medidas.view_medida', 'medidas.view_impacto', 'medidas.view_objetivo',
                      'medidas.view_indicadordecumplimiento'), raise_exception=True)
@transaction.atomic
def medida_form_view(request, pk=None): # pylint: disable=invalid-name
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
        impacto_formset = ImpactoFormSet(request.POST, instance=medida)
        objetivo_formset = ObjetivoFormSet(request.POST, instance=medida)
        indicador_formset = IndicadorDeCumplimientoFormSet(
            request.POST, instance=medida)
        if medida_form.is_valid():
            medida_form.save()

            if impacto_formset.is_valid() and objetivo_formset.is_valid() and\
                indicador_formset.is_valid():
                impacto_formset.save()
                objetivo_formset.save()
                indicador_formset.save()
                return redirect('medidas:lista-medidas')
    return render(request, 'medidas/form.html', {
        'medida_form': medida_form,
        'impacto_formset': impacto_formset,
        'objetivo_formset': objetivo_formset,
        'indicador_formset': indicador_formset,
    })
