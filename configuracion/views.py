"""aa
"""
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from configuracion.forms import EstudioForm
from configuracion.models import Estudio, Intensidad, Duracion, Extension
from configuracion.models import Reversibilidad, Probabilidad, Importancia
from configuracion.models import GRADO_PERTUBACION
from configuracion.models import VALOR_SA, EXT_CLASIFICACION, DUR_CRITERIOS
from configuracion.models import REV_CLASIFICACION, PROBABILIDAD

def index(request):
    """Index de los impactos y listado de los mismos
    """

    estudios_fisicos = Estudio.objects.filter(tipo="FS")
    estudios_biologicos = Estudio.objects.filter(tipo="BIO")
    estudios_socioculturales = Estudio.objects.filter(tipo="SC")

    cant_fisicos = estudios_fisicos.count()
    cant_biologicos = estudios_biologicos.count()
    cant_socioculturales = estudios_socioculturales.count()

    maximo = max([cant_fisicos, cant_biologicos, cant_socioculturales])
    lista = []
    for i in range(0, maximo):
        lista.append([])

    for i in range(0, maximo):
        if i < cant_fisicos:
            lista[i].append(estudios_fisicos[i])
        else:
            lista[i].append(None)

    for i in range(0, maximo):
        if i < cant_biologicos:
            lista[i].append(estudios_biologicos[i])
        else:
            lista[i].append(None)

    for i in range(0, maximo):
        if i < cant_socioculturales:
            lista[i].append(estudios_socioculturales[i])
        else:
            lista[i].append(None)

    return render(request, 'configuracion/index.html', {'lista':lista})

class EstudioCreate(CreateView, SuccessMessageMixin): # pylint: disable=too-many-ancestors
    """Formulario para registrar un estudio/impacto
    """
    model = Estudio
    form_class = EstudioForm
    template_name = 'configuracion/agregar_estudio.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """asas
        """
        # pylint: disable=attribute-defined-outside-init
        self.object = form.save(commit=False)
        self._asignar_valores_estudio()

        messages.success(self.request, "Estudio agregado exitosamente", extra_tags='alert')
        return super().form_valid(form)

    def _asignar_valores_estudio(self):
        """asas
        """
        grado_perturbacion = self.request.POST.get('grado_perturbacion')
        valor_sa = self.request.POST.get('valor_sociocultural')
        ext_clasificacion = self.request.POST.get('clasificacion_extension')
        dur_criterios = self.request.POST.get('criterio_duracion')
        rev_clasificacion = self.request.POST.get('clasificacion_reversibilidad')
        probabilidad = self.request.POST.get('clasificacion_probabilidad')

        val_intensidad = 0
        val_duracion = 0
        val_reversibilidad = 0
        val_extension = 0
        val_probabilidad = 0

        for i in Intensidad.objects.all():
            if (dict(VALOR_SA).get(i.valor_sociocultural) == valor_sa and
                    dict(GRADO_PERTUBACION).get(i.grado_perturbacion) == grado_perturbacion):
                self.object.intensidad = i
                val_intensidad = i.valor
                break

        for i in Extension.objects.all():
            if dict(EXT_CLASIFICACION).get(i.clasificacion) == ext_clasificacion:
                self.object.extension = i
                val_extension = i.valor
                break

        for i in Duracion.objects.all():
            if dict(DUR_CRITERIOS).get(i.criterio) == dur_criterios:
                self.object.duracion = i
                val_duracion = i.valor
                break

        for i in Reversibilidad.objects.all():
            if dict(REV_CLASIFICACION).get(i.clasificacion) == rev_clasificacion:
                self.object.reversibilidad = i
                val_reversibilidad = i.valor
                break

        for i in Probabilidad.objects.all():
            if dict(PROBABILIDAD).get(i.probabilidad) == probabilidad:
                self.object.probabilidad = i
                val_probabilidad = i.valor
                break

        self.object.via = _calcular_via(self.object, val_intensidad, val_duracion,
                                        val_reversibilidad, val_extension, val_probabilidad)

        for i in Importancia.objects.all():
            if i.minimo <= self.object.via <= i.maximo:
                self.object.importancia_estudio = i
                break

        self.object.save()

    @classmethod
    def grado_perturbacion(cls):
        """aa
        """

        grado_pertubacion = (
            'Fuerte',
            'Medio',
            'Suave'
            )
        return grado_pertubacion

    @classmethod
    def valor_sa(cls):
        """aa
        """
        valor_sa = (
            'Muy Alto',
            'Alto',
            'Medio',
            'Bajo'
            )
        return valor_sa

    @classmethod
    def ext_clasificacion(cls):
        """aa
        """
        ext_clasificacion = (
            'Generalizada (>75%)',
            'Extensiva (35-74%)',
            'Local (10-34%)',
            'Puntual (<10%)'
            )
        return ext_clasificacion

    @classmethod
    def dur_criterios(cls):
        """aa
        """
        dur_criterios = (
            'Menos de 2 años',
            '2 a 5 años',
            '5 a 10 años',
            'Mas de 10 años'
            )
        return dur_criterios

    @classmethod
    def rev_clasificacion(cls):
        """aa
        """
        rev_clasificacion = (
            'Irreversible',
            'Requiere Tratamiento',
            'Medianamente Reversible',
            'Reversible'
            )
        return rev_clasificacion

    @classmethod
    def probabilidad(cls):
        """aa
        """
        probabilidad = (
            'Alta',
            'Media',
            'Baja',
            'Nula'
            )
        return probabilidad

class EstudioUpdate(UpdateView, SuccessMessageMixin): # pylint: disable=too-many-ancestors
    """Actualizacion de los datos del formulario
    """
    model = Estudio
    form_class = EstudioForm
    template_name = 'configuracion/agregar_estudio.html'
    success_message = "Datos del Estudio actualizados correctamente"

    def form_valid(self, form):
        """aa
        """
        if self.request.POST.get('editar'):
            # pylint: disable=attribute-defined-outside-init
            self.object = form.save(commit=False)
            self._asignar_valores_estudio()

            messages.success(
                self.request,
                "Datos del estudio modificados exitosamente",
                extra_tags='alert'
                )
        return super().form_valid(form)

    def _asignar_valores_estudio(self):
        """asas
        """
        grado_perturbacion = self.request.POST.get('grado_perturbacion')
        valor_sa = self.request.POST.get('valor_sociocultural')
        ext_clasificacion = self.request.POST.get('clasificacion_extension')
        dur_criterios = self.request.POST.get('criterio_duracion')
        rev_clasificacion = self.request.POST.get('clasificacion_reversibilidad')
        probabilidad = self.request.POST.get('clasificacion_probabilidad')

        val_intensidad = 0
        val_duracion = 0
        val_reversibilidad = 0
        val_extension = 0
        val_probabilidad = 0

        for i in Intensidad.objects.all():
            if (dict(VALOR_SA).get(i.valor_sociocultural) == valor_sa and
                    dict(GRADO_PERTUBACION).get(i.grado_perturbacion) == grado_perturbacion):
                self.object.intensidad = i
                val_intensidad = i.valor
                break

        for i in Extension.objects.all():
            if dict(EXT_CLASIFICACION).get(i.clasificacion) == ext_clasificacion:
                self.object.extension = i
                val_extension = i.valor
                break

        for i in Duracion.objects.all():
            if dict(DUR_CRITERIOS).get(i.criterio) == dur_criterios:
                self.object.duracion = i
                val_duracion = i.valor
                break

        for i in Reversibilidad.objects.all():
            if dict(REV_CLASIFICACION).get(i.clasificacion) == rev_clasificacion:
                self.object.reversibilidad = i
                val_reversibilidad = i.valor
                break

        for i in Probabilidad.objects.all():
            if dict(PROBABILIDAD).get(i.probabilidad) == probabilidad:
                self.object.probabilidad = i
                val_probabilidad = i.valor
                break

        self.object.via = _calcular_via(self.object, val_intensidad, val_duracion,
                                        val_reversibilidad, val_extension, val_probabilidad)

        for i in Importancia.objects.all():
            if i.minimo <= self.object.via <= i.maximo:
                self.object.importancia_estudio = i
                break

        self.object.save()

    @classmethod
    def grado_perturbacion(cls):
        """aa
        """

        grado_pertubacion = (
            'Fuerte',
            'Medio',
            'Suave'
            )
        return grado_pertubacion

    @classmethod
    def valor_sa(cls):
        """aa
        """
        valor_sa = (
            'Muy Alto',
            'Alto',
            'Medio',
            'Bajo'
            )
        return valor_sa

    @classmethod
    def ext_clasificacion(cls):
        """aa
        """
        ext_clasificacion = (
            'Generalizada (>75%)',
            'Extensiva (35-74%)',
            'Local (10-34%)',
            'Puntual (<10%)'
            )
        return ext_clasificacion

    @classmethod
    def dur_criterios(cls):
        """aa
        """
        dur_criterios = (
            'Menos de 2 años',
            '2 a 5 años',
            '5 a 10 años',
            'Mas de 10 años'
            )
        return dur_criterios

    @classmethod
    def rev_clasificacion(cls):
        """aa
        """
        rev_clasificacion = (
            'Irreversible',
            'Requiere Tratamiento',
            'Medianamente Reversible',
            'Reversible'
            )
        return rev_clasificacion

    @classmethod
    def probabilidad(cls):
        """aa
        """
        probabilidad = (
            'Alta',
            'Media',
            'Baja',
            'Nula'
            )
        return probabilidad

    def get_success_url(self):
        """aa
        """
        if self.request.POST.get('editar'):
            return reverse('index')
        return reverse('index')

# pylint: disable=too-many-arguments
def _calcular_via(estudio, valor_intensidad, valor_duracion, valor_reversibilidad,
                  valor_extension, valor_probabilidad):
    """Calculo del VIA
    """
    inte = valor_intensidad*(estudio.pondIntensidad/100)
    dur = valor_extension*(estudio.pondExtension/100)
    ext = valor_duracion*(estudio.pondDuracion/100)
    rev = valor_reversibilidad*(estudio.pondReversibilidad/100)
    prob = valor_probabilidad*(estudio.pondProbabilidad/100)

    return inte + dur + ext + rev + prob

def eliminar_estudio(request, pk_id):
    """Funcion que elimina un estudio
    """
    Estudio.objects.get(id=pk_id).delete()
    messages.success(request, "Estudio eliminado exitosamente", extra_tags='alert')
    return HttpResponseRedirect(reverse('index'))

def modificar_tablas(request):
    """aa
    """
    intensidad_fuerte = Intensidad.objects.all().filter(grado_perturbacion='F')
    intensidad_medio = Intensidad.objects.all().filter(grado_perturbacion='M')
    intensidad_suave = Intensidad.objects.all().filter(grado_perturbacion='S')
    extension = Extension.objects.all().order_by('id')
    duracion = Duracion.objects.all().order_by('id')
    reversibilidad = Reversibilidad.objects.all().order_by('id')
    probabilidad = Probabilidad.objects.all().order_by('id')
    importancia = Importancia.objects.all().order_by('id')

    context = {
        'intensidad_fuerte':intensidad_fuerte,
        'intensidad_medio':intensidad_medio,
        'intensidad_suave':intensidad_suave,
        'extension':extension,
        'duracion':duracion,
        'reversibilidad':reversibilidad,
        'probabilidad':probabilidad,
        'importancia': importancia,
    }

    if request.method == 'POST':
        if request.POST.get('submit'):
            _conseguir_valor_tabla_intensidad_fuerte(request, intensidad_fuerte)
            _conseguir_valor_tabla_intensidad_medio(request, intensidad_medio)
            _conseguir_valor_tabla_intensidad_suave(request, intensidad_suave)
            _conseguir_valor_tabla_extension(request, extension)
            _conseguir_valor_tabla_duracion(request, duracion)
            _conseguir_valor_tabla_reversibilidad(request, reversibilidad)
            _conseguir_valor_tabla_probabilidad(request, probabilidad)
            _conseguir_valor_tabla_importancia(request, importancia)

            messages.success(request, "Datos modificados exitosamente", extra_tags='alert')
        return redirect('/configuracion/tablas/')

    return render(request, 'configuracion/modificar_tablas.html', context)

def tablas(request):
    """aa
    """
    intensidad_fuerte = Intensidad.objects.all().filter(grado_perturbacion='F')
    intensidad_medio = Intensidad.objects.all().filter(grado_perturbacion='M')
    intensidad_suave = Intensidad.objects.all().filter(grado_perturbacion='S')
    extension = Extension.objects.all().order_by('id')
    duracion = Duracion.objects.all().order_by('id')
    reversibilidad = Reversibilidad.objects.all().order_by('id')
    probabilidad = Probabilidad.objects.all().order_by('id')
    importancia = Importancia.objects.all().order_by('id')
    context = {
        'intensidad_fuerte':intensidad_fuerte,
        'intensidad_medio':intensidad_medio,
        'intensidad_suave':intensidad_suave,
        'extension':extension,
        'duracion':duracion,
        'reversibilidad':reversibilidad,
        'probabilidad':probabilidad,
        'importancia': importancia,
    }

    return render(request, 'configuracion/tablas.html', context)

def _conseguir_valor_tabla_intensidad_fuerte(request, intensidad_fuerte):
    """aaa
    """
    for i in intensidad_fuerte:
        if i.valor_sociocultural == 'MA':
            i.valor = request.POST.get('valor1')
            i.save()
        elif i.valor_sociocultural == 'A':
            i.valor = request.POST.get('valor2')
            i.save()
        elif i.valor_sociocultural == 'M':
            i.valor = request.POST.get('valor3')
            i.save()
        else:
            i.valor = request.POST.get('valor4')
            i.save()

def _conseguir_valor_tabla_intensidad_medio(request, intensidad_medio):
    """aaa
    """
    for i in intensidad_medio:
        if i.valor_sociocultural == 'MA':
            i.valor = request.POST.get('valor5')
            i.save()
        elif i.valor_sociocultural == 'A':
            i.valor = request.POST.get('valor6')
            i.save()
        elif i.valor_sociocultural == 'M':
            i.valor = request.POST.get('valor7')
            i.save()
        else:
            i.valor = request.POST.get('valor8')
            i.save()

def _conseguir_valor_tabla_intensidad_suave(request, intensidad_suave):
    """aaa
    """
    for i in intensidad_suave:
        if i.valor_sociocultural == 'MA':
            i.valor = request.POST.get('valor9')
            i.save()
        elif i.valor_sociocultural == 'A':
            i.valor = request.POST.get('valor10')
            i.save()
        elif i.valor_sociocultural == 'M':
            i.valor = request.POST.get('valor11')
            i.save()
        else:
            i.valor = request.POST.get('valor12')
            i.save()

def _conseguir_valor_tabla_extension(request, extension):
    """aaa
    """
    for i in extension:
        if i.clasificacion == 'GE':
            i.valor = request.POST.get('valor13')
            i.save()
        elif i.clasificacion == 'EX':
            i.valor = request.POST.get('valor14')
            i.save()
        elif i.clasificacion == 'LO':
            i.valor = request.POST.get('valor15')
            i.save()
        else:
            i.valor = request.POST.get('valor16')
            i.save()

def _conseguir_valor_tabla_duracion(request, duracion):
    """aaa
    """
    for i in duracion:
        if  i.criterio == 'M2':
            i.valor = request.POST.get('valor17')
            i.save()
        elif i.criterio == 'M2-5':
            i.valor = request.POST.get('valor18')
            i.save()
        elif i.criterio == 'M5-10':
            i.valor = request.POST.get('valor19')
            i.save()
        else:
            i.valor = request.POST.get('valor20')
            i.save()

def _conseguir_valor_tabla_reversibilidad(request, reversibilidad):
    """aaa
    """
    for i in reversibilidad:
        if  i.clasificacion == 'IR':
            i.valor = request.POST.get('valor21')
            i.save()
        elif i.clasificacion == 'TR':
            i.valor = request.POST.get('valor22')
            i.save()
        elif i.clasificacion == 'MR':
            i.valor = request.POST.get('valor23')
            i.save()
        else:
            i.valor = request.POST.get('valor24')
            i.save()

def _conseguir_valor_tabla_probabilidad(request, probabilidad):
    """aaa
    """
    for i in probabilidad:
        if  i.probabilidad == 'A':
            i.valor = request.POST.get('valor25')
            i.save()
        elif i.probabilidad == 'M':
            i.valor = request.POST.get('valor26')
            i.save()
        elif i.probabilidad == 'B':
            i.valor = request.POST.get('valor27')
            i.save()
        else:
            i.valor = request.POST.get('valor28')
            i.save()

def _conseguir_valor_tabla_importancia(request, importancia):
    """aaa
    """
    for i in importancia:
        if  i.importancia == 'MA':
            i.valor = request.POST.get('valor29')
            i.save()
        elif i.importancia == 'A':
            i.valor = request.POST.get('valor30')
            i.save()
        elif i.importancia == 'M':
            i.valor = request.POST.get('valor31')
            i.save()
        else:
            i.valor = request.POST.get('valor32')
            i.save()
