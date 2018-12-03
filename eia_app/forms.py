'''Forms para el uso del crud del consultor'''

from django import forms
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
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
        fields = '__all__'


class DatosDocumentoCreateForm(forms.ModelForm):
    '''Form del modelo datos de documentos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DatosDocumento
        fields = '__all__'


class DescripcionProyectoCreateForm(forms.ModelForm):
    '''Form del modelo descripcion de proyectos'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Clase meta del formulario'''
        model = DescripcionProyecto
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
