'''Forms para el uso del crud del consultor'''

from django import forms
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto
)


class OrganizacionCreateForm(forms.ModelForm):
    '''Form del modelo organizacion'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Organizacion
        fields = '__all__'


class SolicitanteCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Solicitante
        fields = '__all__'


class ResponsableCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Responsable
        fields = '__all__'


class DatosProyectoCreateForm(forms.ModelForm):
    '''Form del modelo datos proyecto'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DatosProyecto
        fields = ('titulo', 'ubicacion', 'area', 'tipo', 'url')


class DatosDocumentoCreateForm(forms.ModelForm):
    '''Form del modelo datos de documentos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DatosDocumento
        fields = '__all__'

class MarcoForm(forms.Form):
    """Form para el marco (metodologico, juridico o teorico) de un proyecto."""
    proyecto = forms.ModelChoiceField(DatosProyecto.objects.all(), label='Proyecto')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')

class DescripcionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo descripcion de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DescripcionProyecto
        fields = '__all__'
