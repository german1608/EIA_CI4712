'''Forms para el uso de lista de medidas'''

from django import forms
from django.forms import inlineformset_factory
from .models import (
    Medida, Impacto, IndicadorDeCumplimiento, Objetivo
)


class MedidaForm(forms.ModelForm):
    '''Form del modelo medida'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Medida
        fields = '__all__'

# pylint: disable=invalid-name
ImpactoFormSet = inlineformset_factory(Medida, Impacto, can_delete=True)
ObjetivoFormSet = inlineformset_factory(Medida, Objetivo, can_delete=True)
IndicadorDeCumplimientoFormSet = inlineformset_factory(
    Medida, IndicadorDeCumplimiento, can_delete=True)
