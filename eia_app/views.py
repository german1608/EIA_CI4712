'''Views del crud del consultor'''

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView,
                                  FormView)
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q
from django.conf import settings
from django_weasyprint import WeasyTemplateResponseMixin
from django.http import Http404
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    RecomendacionProyecto, ConclusionProyecto
)
from .forms import (
    OrganizacionCreateForm, SolicitanteCreateForm,
    DatosProyectoCreateForm, MarcoForm, DescripcionProyectoCreateForm,
    ResponsableCreateForm, DatosDocumentoCreateForm,
    RecomendacionProyectoCreateForm, ConclusionProyectoCreateForm
)


class OrganizacionList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las organizaciones'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/list.html'


class OrganizacionDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/detail.html'


class OrganizacionCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Organizacion
    form_class = OrganizacionCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(OrganizacionCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Organización"
        return context


class OrganizacionUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'


class OrganizacionDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')


class DatosProyectoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar los datos de los proyectos'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/list.html'


class DatosProyectoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear datos de un proyecto'''
    model = DatosProyecto
    form_class = DatosProyectoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Datos de un proyecto"
        return context


class DatosProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    form_class = DatosProyectoCreateForm


class DatosProyectoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')


class DatosProyectoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/detail.html'

class GenerarPDFView(DetailView): # pylint: disable=too-many-ancestors
    '''Vista que se encarga de conectar con el html que servira de modelo de pdf'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/imprimir.html'

class ImprimirDatosDelProyecto(WeasyTemplateResponseMixin, GenerarPDFView): # pylint: disable=too-many-ancestors
    '''Con esta vista se generara el pdf con los detalles del proyect'''
    pdf_stylesheets = [
        'static/css/generacion_pdf.css',
    ]


class ResponsableList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Responsables'''
    model = Responsable
    template_name = 'eia_app/responsables/list.html'


class ResponsableDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/detail.html'


class ResponsableCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Responsable'''
    model = Responsable
    form_class = ResponsableCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(ResponsableCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Responsable"
        return context


class ResponsableUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Responsable'''
    model = Responsable
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    fields = '__all__'


class ResponsableDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')


class SolicitanteList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Solicitantes'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/list.html'


class SolicitanteDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/detail.html'


class SolicitanteCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Solicitante'''
    model = Solicitante
    form_class = SolicitanteCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SolicitanteCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Solicitante"
        return context


class SolicitanteUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    fields = '__all__'


class SolicitanteDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')


class DatosDocumentoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DatosDocumentos'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/list.html'


class DatosDocumentoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/detail.html'


class DatosDocumentoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DatosDocumento'''
    model = DatosDocumento
    form_class = DatosDocumentoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosDocumentoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Datos de un documento"
        return context


class DatosDocumentoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    fields = '__all__'


class DatosDocumentoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')

class CargaContextoMarcoMixin(LoginRequiredMixin, ContextMixin): # pylint: disable=too-few-public-methods
    '''
    Mixin que anade contexto adicional a las vistas de marcos.
    Anade el tipo de marco a editar acentuado (para mostrarlo al usuario)
    y sin acentuar (para uso en {% url %})
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.kwargs.get('tipo')
        context['tipo'] = tipo
        if tipo == 'metodologico':
            tipo_marco = 'metodológico'
        elif tipo == 'teorico':
            tipo_marco = 'teórico'
        else:
            tipo_marco = 'jurídico'
        context['tipo_marco'] = tipo_marco
        return context


class MarcoListView(CargaContextoMarcoMixin, ListView): # pylint: disable=too-many-ancestors
    '''
    Lista los marcos del sistema
    Toma los siguientes parametros:
        tipo: (metodologico|juridico|teorico) Tipo de marco a listar
    '''
    template_name = 'eia_app/marco/list.html'
    model = DatosProyecto

    def get_queryset(self):
        query = {
            'marco_{tipo}'.format(tipo=self.kwargs.get('tipo')): None
        }
        # Filtramos los que no esten en None
        return self.model.objects.filter(~Q(**query))


class MarcoFormView(CargaContextoMarcoMixin, FormView):
    """ Vista que permite crear un marco metodologico a un proyecto """
    form_class = MarcoForm
    template_name = 'eia_app/marco/form.html'
    success_url = reverse_lazy('consultor-crud:lista-marcos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edicion'] = self.kwargs.get('pk', None) is not None
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk_proyecto = self.kwargs.get('pk', None)
        if pk_proyecto is None:
            return kwargs
        proyecto = DatosProyecto.objects.get(pk=pk_proyecto)
        tipo = self.kwargs.get('tipo')
        if tipo == 'metodologico':
            contenido = proyecto.marco_metodologico
        elif tipo == 'teorico':
            contenido = proyecto.marco_teorico
        else:
            contenido = proyecto.marco_juridico
        kwargs['initial']['contenido'] = contenido
        kwargs['initial']['proyecto'] = pk_proyecto
        return kwargs

    def form_valid(self, form):
        tipo = self.kwargs.get('tipo')
        self.success_url = reverse_lazy('consultor-crud:lista-marcos', kwargs={
            'tipo': tipo
        })
        proyecto = form.cleaned_data['proyecto']
        contenido = form.cleaned_data['contenido']
        if tipo == 'metodologico':
            proyecto.marco_metodologico = contenido
        elif tipo == 'juridico':
            proyecto.marco_juridico = contenido
        else:
            proyecto.marco_teorico = contenido

        proyecto.save()
        return super().form_valid(form)

class MarcoDetailView(CargaContextoMarcoMixin, DetailView): # pylint: disable=too-many-ancestors
    ''' Vista para mostrar un marco de un proyecto '''
    template_name = "eia_app/marco/detail.html"
    model = DatosProyecto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = context['tipo']
        if tipo == 'metodologico':
            contenido = self.object.marco_metodologico
        elif tipo == 'teorico':
            contenido = self.object.marco_teorico
        else:
            contenido = self.object.marco_juridico
        context['contenido'] = contenido
        return context

    def get(self, request, *a, **kw):
        response = super().get(request, *a, **kw)
        proyecto = self.object
        tipo = kw.get('tipo')
        marco = getattr(proyecto, 'marco_' + tipo)
        if marco is None:
            raise Http404('El proyecto no tiene marco ' + tipo + ' asociado')
        return response

@login_required
def delete_marco_view(request, tipo, pk): # pylint: disable=invalid-name
    '''
    Maneja la eliminacion de marcos. La eliminacion de marcos consiste
    el igualar el atributo a NULL
    Argumentos:
        - tipo: tipo de marco a eliminar (metodologico|juridico|teorico)
        - pk: Primary key del proyecto cuyo marco se eliminara
    '''
    proyecto = get_object_or_404(DatosProyecto, **{'pk': pk})
    if request.method == 'GET':
        if tipo == 'metodologico':
            contenido = proyecto.marco_metodologico
            tipo_marco = 'metodológico'
        elif tipo == 'teorico':
            contenido = proyecto.marco_teorico
            tipo_marco = 'teórico'
        else:
            contenido = proyecto.marco_juridico
            tipo_marco = 'jurídico'
        if contenido is None:
            raise Http404('El proyecto escogido no tiene marco {} asociado'.format(tipo))
        return render(request, 'eia_app/marco/delete.html',
                      {'object':proyecto, 'contenido': contenido, 'tipo_marco': tipo_marco})

    if tipo == 'metodologico':
        proyecto.marco_metodologico = None
    elif tipo == 'juridico':
        proyecto.marco_juridico = None
    else:
        proyecto.marco_teorico = None
    proyecto.save()
    return redirect(reverse_lazy('consultor-crud:lista-marcos', kwargs={'tipo': tipo}))

class DescripcionProyectoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/list.html'


class DescripcionProyectoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/detail.html'


class DescripcionProyectoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DescripcionProyecto'''
    model = DescripcionProyecto
    form_class = DescripcionProyectoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DescripcionProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Detalles de un documento"
        return context


class DescripcionProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    fields = '__all__'


class DescripcionProyectoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

class RecomendacionProyectoCreateUpdateBase:
    model = RecomendacionProyecto
    form_class = RecomendacionProyectoCreateForm
    template_name = 'eia_app/recomendaciones_proyecto/form.html'
    success_url = reverse_lazy('consultor-crud:lista-recomendaciones-proyecto')

class RecomendacionProyectoCreateView(RecomendacionProyectoCreateUpdateBase, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una RecomendacionProyecto'''


class RecomendacionProyectoUpdateView(RecomendacionProyectoCreateUpdateBase, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una RecomendacionProyecto'''

class RecomendacionProyectoDetailView(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DescripcionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/detail.html'

class RecomendacionProyectoDeleteView(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una RecomendacionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-recomendaciones-proyecto')

class RecomendacionProyectoListView(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las RecomendacionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/list.html'


def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)



class ConclusionesListView(ListView):
    'Lista de las conclusiones de todos los proyectos'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/list.html'

class ConclusionAddOrEditBase:
    ''' Clase base para la edicion y creacion de conclusiones '''
    model = ConclusionProyecto
    form_class = ConclusionProyectoCreateForm
    template_name = 'eia_app/conclusiones/form.html'
    success_url = reverse_lazy('consultor-crud:lista-conclusiones')


class ConclusionesCreateView(ConclusionAddOrEditBase, CreateView):
    'Crear una conclusión para un proyecto'

class ConclusionUpdateView(ConclusionAddOrEditBase, UpdateView):
    'Actualizar datos de una conclusión'

class ConclusionDeleteView(DeleteView):
    'Eliminar una conclusión de un proyecto'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-conclusiones')

class ConclusionDetailView(DetailView):
    'Detalles acerca de una conclusión de un proyecto'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/detail.html'
