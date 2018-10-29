'''Forms para el uso del crud del consultor'''

from django import forms
from .models import * #pylint: disable=unused-wildcard-import, wildcard-import

class OrganizacionCreateForm(forms.ModelForm):
    '''Form del modelo organizacion'''
    class Meta: # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Organizacion
        fields = '__all__'

class SolicitanteCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta: # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Solicitante
        fields = '__all__'

class ResponsableCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta: # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Responsable
        fields = '__all__'