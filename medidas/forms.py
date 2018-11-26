'''Forms para el uso de lista de medidas'''

from django import forms
from .models import (
    Medida
)


class MedidaCreateForm(forms.ModelForm):
    '''Form del modelo medida'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Medida
        fields = '__all__'
