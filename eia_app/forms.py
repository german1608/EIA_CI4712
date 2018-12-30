'''Forms para el uso del crud del consultor'''

from django import forms
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    RecomendacionProyecto, ConclusionProyecto
)


class OrganizacionCreateForm(forms.ModelForm):
    '''Form del modelo organizacion'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Organizacion
        fields = ('razon_social', 'nombre', 'rif', 'direccion', 'nombre_representante_legal', 'apellido_representante_legal'
                    , 'cedula_representante_legal', 'pasaporte_representante_legal', 'telefono', 'email')


class SolicitanteCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Solicitante
        fields = ('nombre', 'apellido', 'cedula', 'pasaporte', 'telefono', 'email')


class ResponsableCreateForm(forms.ModelForm):
    '''Form del modelo solicitante'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = Responsable
        fields = ('nombre', 'apellido', 'cedula', 'pasaporte', 'nivel_academico', 'tipo_responsable')


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
        fields = ('fecha', 'ciudad', 'estado', 'pais')

class MarcoForm(forms.Form):
    """Form para el marco (metodologico, juridico o teorico) de un proyecto."""
    proyecto = forms.ModelChoiceField(DatosProyecto.objects.all(), label='Proyecto')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')

class DescripcionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo descripcion de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DescripcionProyecto
        fields = ('obj_general', 'obj_especifico', 'justificacion', 'area')

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
