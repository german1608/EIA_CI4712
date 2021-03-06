'''Forms para el uso del crud del consultor'''

from django import forms
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    RecomendacionProyecto, ConclusionProyecto,
    Medio, CaracteristicaMedio, SubaracteristicaMedio
)


class OrganizacionCreateForm(forms.ModelForm):
    '''Form del modelo organizacion'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Organizacion
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude


class SolicitanteCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Solicitante
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class ResponsableCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Responsable
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class DatosProyectoCreateForm(forms.ModelForm):
    '''Form del modelo datos proyecto'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DatosProyecto
        fields = ('titulo', 'ubicacion', 'area', 'tipo')
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude


class DatosDocumentoCreateForm(forms.ModelForm):
    '''Form del modelo datos de documentos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DatosDocumento
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class MarcoForm(forms.Form):
    """Form para el marco (metodologico, juridico o teorico) de un proyecto."""
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')

class DescripcionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo descripcion de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DescripcionProyecto
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class RecomendacionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo recomendaciones de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = RecomendacionProyecto
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class ConclusionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo conclusiones de proyectos'''
    class Meta: # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = ConclusionProyecto
        fields = ['conclusiones']

class MedioCreateForm(forms.ModelForm):
    '''Form del modelo medio'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Medio
        fields = '__all__'
        exclude = ['proyecto'] # pylint: disable=modelform-uses-exclude

class CaracteristicaMedioCreateForm(forms.ModelForm):
    '''Form del modelo medio'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = CaracteristicaMedio
        fields = '__all__'

class SubaracteristicaMedioCreateForm(forms.ModelForm):
    '''Form del modelo medio'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = SubaracteristicaMedio
        fields = '__all__'
