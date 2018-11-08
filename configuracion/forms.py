"""Formularios de Configuracion
"""
from django import forms
from configuracion.models import Estudio, Intensidad, Duracion, Extension
from configuracion.models import Reversibilidad, Probabilidad, Importancia

class EstudioForm(forms.ModelForm):
    """Formulario de Estudio
    """

    class Meta:
        """ Meta del formulario de Estudio
        """
        model = Estudio
        fields = [
            'nombre',
            'tipo',
            'valoracion_relevancia',
            'tipo_relevancia',
            'pondIntensidad',
            'pondExtension',
            'pondDuracion',
            'pondReversibilidad',
            'pondProbabilidad',
        ]

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo de Estudio',
            'valoracion_relevancia' : 'Relevancia',
            'tipo_relevancia': 'Tipo de Relevancia',
            'pondIntensidad': 'Ponderación de la Intensidad',
            'pondExtension': 'Ponderación de la Extensión',
            'pondDuracion': 'Ponderación de la Duración',
            'pondReversibilidad': 'Ponderación de la Reversibilidad',
            'pondProbabilidad': 'Ponderación de la Probabilidad',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'browser-default', 'required':''}),
            'tipo': forms.Select(attrs={'class':'browser-default', 'required':''}),
            'valoracion_relevancia':forms.Select(attrs={'class':'browser-default', 'required':''}),
            'tipo_relevancia': forms.Select(attrs={'class':'browser-default', 'required':''}),
            'pondIntensidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondExtension': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondDuracion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondReversibilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondProbabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            }

class IntesidadForm(forms.ModelForm):
    """Formulario de Intensidad
    """

    class Meta:
        """Meta del formulario de Intensidad
        """

        model = Intensidad
        fields = [
            'valor_sociocultural',
            'grado_perturbacion',
            'valor',

        ]

        labels = {
            'valor_sociocultural':'Valor Socio Cultural',
            'grado_perturbacion':'Grado de Perturbación',
            'valor': 'Valor',

        }

        widgets = {
            'valor_sociocultural':forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'grado_perturbacion':forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'valor':forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }

class ExtensionForm(forms.ModelForm):
    """FOrmulario de Extension
    """

    class Meta:
        """Meta del formulario de Extension
        """

        model = Extension
        fields = [
            'clasificacion',
            'valor',

        ]

        labels = {
            'clasificacion':'Criterio de Duración',
            'valor':'Valor',

        }

        widgets = {
            'clasificacion':forms.Select(attrs={'class':'form-control', 'required':''}),
            'valor':forms.TextInput(attrs={'class':'form-control', 'required':''}),

        }

class DuracionForm(forms.ModelForm):
    """Formulario de Duracion
    """

    class Meta:
        """Meta del formulario Duracion
        """

        model = Duracion
        fields = [
            'criterio',
            'valor',

        ]

        labels = {
            'criterio':'Criterio de Clasificacion',
            'valor':'Valor',
        }

        widgets = {
            'criterio':forms.Select(attrs={'class':'form-control', 'required':''}),
            'valor':forms.TextInput(attrs={'class':'form-control', 'required':''}),

        }

class ReversibilidadForm(forms.ModelForm):
    """Formulario de Reversibilidad
    """

    class Meta:
        """Meta del formulario de Reversibilidad
        """

        model = Reversibilidad
        fields = [
            'clasificacion',
            'valor',

        ]

        labels = {
            'clasificacion':'Clasificacion de Reversibilidad',
            'valor':'Valor',
        }

        widgets = {
            'clasificacion':forms.Select(attrs={'class':'form-control', 'required':''}),
            'valor':forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }

class ProbabilidadForm(forms.ModelForm):
    """Formulario de Probabilidad
    """

    class Meta:
        """Meta del Formulario de Probabilidad
        """

        model = Probabilidad
        fields = [
            'probabilidad',
            'valor',

        ]

        labels = {
            'probabilidad':'Probabilidad',
            'valor':'Valor',
        }

        widgets = {
            'probabilidad':forms.Select(attrs={'class':'form-control', 'required':''}),
            'valor':forms.TextInput(attrs={'class':'form-control', 'required':''}),

        }

class ImportanciaForm(forms.ModelForm):
    """Formulario de Importancia
    """

    class Meta:
        """ Meta del Formulario Importancia
        """
        model = Importancia
        fields = [
            'importancia',
            'minimo',
            'maximo',
            'valor',
        ]

        labels = {
            'importancia':'Importancia',
            'minimo':'Minimo valor',
            'maximo':'Maximo valor',
            'valor': 'Valor',

        }

        widgets = {
            'importancia':forms.Select(attrs={'class':'form-control', 'required':''}),
            'minimo': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'maximo':forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'valor': forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }
        