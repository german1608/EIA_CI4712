"""
   Formularios de Configuracion
"""
from django import forms
from configuracion.models import Estudio, Intensidad, Duracion, Extension
from configuracion.models import Reversibilidad, Probabilidad, Importancia
from configuracion.models import Macro, Disciplina, Actividad, Plan, SubPlan

class EstudioForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de Estudio
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Estudio
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
            'nombre': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'tipo': forms.Select(attrs={'class':'form-control', 'required':''}),
            'valoracion_relevancia':forms.Select(attrs={'class':'form-control', 'required':''}),
            'tipo_relevancia': forms.Select(attrs={'class':'form-control', 'required':''}),
            'pondIntensidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondExtension': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondDuracion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondReversibilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pondProbabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            }

class IntesidadForm(forms.ModelForm):
    """
        Clase donde se crea el formulario de Intensidad
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Intensidad
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
    """
       Clase donde se crea el formulario de Extension
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Extension
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
    """
       Clase donde se crea el formulario de Duracion
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Duracion
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
    """
       Clase donde se crea el formulario de Reversibilidad
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Reversibilidad
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
    """
       Clase donde se crea el formulario de Probabilidad
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Probabilidad
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
    """
       Clase donde se crea el formulario de Importancia
    """

    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Importancia
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

class MacroForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de Macro
    """
    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Macro
        """
        model = Macro
        fields = [
            'nombre',
            'descripcion',
            'proyecto'
        ]
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'proyecto': 'Proyecto'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'descripcion':forms.Textarea(attrs={'class':'form-control', 'required':''}),
            'proyecto':forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }

class DisciplinaForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de Disciplina
    """
    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Disciplina
        """
        model = Disciplina
        fields = [
            'nombre',
            'descripcion',
            'proyecto',
        ]
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'proyecto': 'Proyecto'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'descripcion':forms.Textarea(attrs={'class':'form-control', 'required':''}),
            'proyecto':forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }

class ActividadForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de Actividad
    """
    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Actividad
        """
        model = Actividad
        fields = [
            'nombre',
            'descripcion',
            'disciplina',
            'macro',
            'amenazas',
            'vulnerabilidades'
        ]
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'disciplina':'Disciplina',
            'macro':'Actividad Macro',
            'amenazas':'Posibles amenazas',
            'vulnerabilidades':'Posibles vulnerabilidades'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mb-3', 'required':''}),
            'descripcion':forms.Textarea(attrs={'class':'form-control mb-3', 'required':''}),
            'disciplina': forms.Select(attrs={'class':'form-control mb-3'}),
            'macro': forms.Select(attrs={'class':'form-control mb-3', 'required':''}),
            'amenazas':forms.Textarea(attrs={'class':'form-control mb-3'}),
            'vulnerabilidades':forms.Textarea(attrs={'class':'form-control mb-3'}),
        }

class PlanForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de Plan
    """
    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de Plan
        """
        model = Plan
        fields = [
            'nombre',
            'medidas',
            'objetivo_general',
            'objetivo_especifico',
            'alcance',
            'metodologia',
            'cronograma',
            'responsable',
            'costo',
            'proyecto'
        ]
        labels = {
            'nombre':'Nombre',
            'medidas':'Medidas',
            'objetivo_general':'Objectivo General',
            'objetivo_especifico':'Objetivos Especificos',
            'alcance':'Alcance',
            'metodologia':'Metodologia a utilizar',
            'cronograma':'Cronograma',
            'responsable':'Responsable(s)',
            'costo':'Costo estimado',
            'proyecto':'Proyecto'
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'medidas':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'objetivo_general':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'objetivo_especifico':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'alcance':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'metodologia':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'cronograma':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'responsable':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'costo':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'proyecto':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
        }

class SubPlanForm(forms.ModelForm):
    """
       Clase donde se crea el formulario de SubPlan
    """
    class Meta:
        """
           Clase donde se indica el modelo que se quiere usar y se crea el
           formulario de SubPLan
        """
        model = SubPlan
        fields = [
            'actividad',
            'accion',
            'plan_principal',
            'tiempo',
            'monto',
        ]
        labels = {
            'actividad':'Actividad a realizar',
            'accion':'Accion a implementar',
            'plan_principal':'Plan de trabajo',
            'tiempo': 'Duracion',
            'monto':'Monto estimado'
        }
        widgets = {
            'actividad':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'accion':forms.Textarea(
                attrs={'class':'form-control mb-3', 'required':''}),
            'plan_principal':forms.Select(
                attrs={'class':'form-control mb-3', 'required':''}),
            'tiempo':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
            'monto':forms.TextInput(
                attrs={'class':'form-control mb-3', 'required':''}),
        }
