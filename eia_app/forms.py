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
        fields = ('titulo', 'ubicacion', 'area', 'tipo')


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

class RecomendacionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo recomendaciones de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = RecomendacionProyecto
        fields = '__all__'

class ConclusionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo conclusiones de proyectos'''
    class Meta: # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = ConclusionProyecto
        fields = '__all__'

class MedioCreateForm(forms.ModelForm):
    '''Form del modelo medio'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Medio
        fields = '__all__'

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
