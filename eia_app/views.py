'''Views del crud del consultor'''
# pylint: disable=too-many-ancestors,too-few-public-methods
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView,
                                  FormView)
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django_weasyprint import WeasyTemplateResponseMixin
from .models import (
    Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    RecomendacionProyecto, ConclusionProyecto, Organizacion,
    CaracteristicaMedio, Medio, SubaracteristicaMedio, CostoHumano, CostoMateriales, TipoCosto
)
from .forms import (
    OrganizacionCreateForm, SolicitanteCreateForm,
    DatosProyectoCreateForm, MarcoForm, DescripcionProyectoCreateForm,
    ResponsableCreateForm, DatosDocumentoCreateForm,
    RecomendacionProyectoCreateForm, ConclusionProyectoCreateForm
)


class OrganizacionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las organizaciones'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/list.html'
    permission_required = 'eia_app.view_organizacion'


class OrganizacionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/detail.html'
    permission_required = 'eia_app.view_organizacion'


class OrganizacionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Organizacion
    form_class = OrganizacionCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    permission_required = 'eia_app.add_organizacion'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(OrganizacionCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar organización"
        return context


class OrganizacionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    permission_required = 'eia_app.change_organizacion'
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(OrganizacionUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar organización"
        return context

class OrganizacionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/delete.html'
    permission_required = 'eia_app.delete_organizacion'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')


class DatosProyectoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar los datos de los proyectos'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/list.html'
    permission_required = 'eia_app.view_datosproyecto'


class DatosProyectoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear datos de un proyecto'''
    model = DatosProyecto
    form_class = DatosProyectoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    permission_required = 'eia_app.add_datosproyecto'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar datos de un proyecto"
        return context

    def form_valid(self, form):
        usuario_loggeado = self.request.user
        # Recupero lo que esta guardado del proyecto
        proyecto = form.save(commit=False)
        # Le agrego el usuario asociado que es el que esta loggeado
        proyecto.usuario = usuario_loggeado
        proyecto.save()
        return HttpResponseRedirect(self.success_url)


class DatosProyectoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    form_class = DatosProyectoCreateForm
    permission_required = 'eia_app.change_datosproyecto'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar datos del proyecto"
        return context


class DatosProyectoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    permission_required = 'eia_app.delete_datosproyecto'


class DatosProyectoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/detail.html'
    permission_required = 'eia_app.view_datosproyecto'

class GenerarPDFView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): # pylint: disable=too-many-ancestors
    '''Vista que se encarga de conectar con el html que servira de modelo de pdf'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/imprimir.html'
    permission_required = 'eia_app.view_datosproyecto'

class ImprimirDatosDelProyecto(WeasyTemplateResponseMixin, GenerarPDFView): # pylint: disable=too-many-ancestors
    '''Con esta vista se generara el pdf con los detalles del proyect'''
    pdf_stylesheets = [
        'static/css/generacion_pdf.css',
    ]
    permission_required = 'eia_app.view_datosproyecto'


class ResponsableList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Responsables'''
    model = Responsable
    template_name = 'eia_app/responsables/list.html'
    permission_required = 'eia_app.view_responsable'


class ResponsableDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/detail.html'
    permission_required = 'eia_app.view_responsable'


class ResponsableCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Responsable'''
    model = Responsable
    form_class = ResponsableCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    permission_required = 'eia_app.add_responsable'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(ResponsableCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar responsable"
        return context


class ResponsableUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Responsable'''
    model = Responsable
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    fields = '__all__'
    permission_required = 'eia_app.change_responsable'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(ResponsableUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar responsable"
        return context


class ResponsableDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    permission_required = 'eia_app.delete_responsable'


class SolicitanteList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Solicitantes'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/list.html'
    permission_required = 'eia_app.view_solicitante'

class SolicitanteDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/detail.html'
    permission_required = 'eia_app.view_solicitante'


class SolicitanteCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Solicitante'''
    model = Solicitante
    form_class = SolicitanteCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    permission_required = 'eia_app.add_solicitante'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SolicitanteCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar solicitante"
        return context


class SolicitanteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    fields = '__all__'
    permission_required = 'eia_app.change_solicitante'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SolicitanteUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar solicitante"
        return context


class SolicitanteDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    permission_required = 'eia_app.delete_solicitante'


class DatosDocumentoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DatosDocumentos'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/list.html'
    permission_required = 'eia_app.view_datosdocumento'


class DatosDocumentoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/detail.html'
    permission_required = 'eia_app.view_datosdocumento'


class DatosDocumentoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DatosDocumento'''
    model = DatosDocumento
    form_class = DatosDocumentoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    permission_required = 'eia_app.add_datosdocumento'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosDocumentoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar datos de un documento"
        return context


class DatosDocumentoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    fields = '__all__'
    permission_required = 'eia_app.change_datosdocumento'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosDocumentoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar datos de un documento"
        return context

class DatosDocumentoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    permission_required = 'eia_app.delete_datosdocumento'

class CargaContextoMarcoMixin(LoginRequiredMixin, ContextMixin, PermissionRequiredMixin): # pylint: disable=too-few-public-methods
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
    permission_required = 'eia_app.view_datosproyecto'
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
    permission_required = 'eia_app.add_datosproyecto'

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
        usuario_loggeado = self.request.user
        pk_proyecto = usuario_loggeado.proyecto_seleccionado
        proyecto = DatosProyecto.objects.get(pk=pk_proyecto)
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
    permission_required = 'eia_app.view_datosproyecto'

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
@permission_required('eia_app.delete_datosproyecto', raise_exception=True)
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

class DescripcionProyectoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/list.html'
    permission_required = 'eia_app.view_descripcionproyecto'


class DescripcionProyectoDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/detail.html'
    permission_required = 'eia_app.view_descripcionproyecto'


class DescripcionProyectoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DescripcionProyecto'''
    model = DescripcionProyecto
    form_class = DescripcionProyectoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    permission_required = 'eia_app.add_descripcionproyecto'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            DescripcionProyectoCreate,
            self).get_context_data(**kwargs)
        context["nombre"] = "Agregar detalles de un documento"
        return context


class DescripcionProyectoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    fields = '__all__'
    permission_required = 'eia_app.change_descripcionproyecto'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            DescripcionProyectoUpdate,
            self).get_context_data(**kwargs)
        context["nombre"] = "Editar detalles de un documento"
        return context


class DescripcionProyectoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    permission_required = 'eia_app.delete_descripcionproyecto'

class RecomendacionProyectoCreateUpdateBase(LoginRequiredMixin, PermissionRequiredMixin): # pylint: disable=too-few-public-methods
    ''' Clase base para la creacion y edicion de recomendaciones '''
    model = RecomendacionProyecto
    form_class = RecomendacionProyectoCreateForm
    template_name = 'eia_app/recomendaciones_proyecto/form.html'
    success_url = reverse_lazy('consultor-crud:lista-recomendaciones-proyecto')

class RecomendacionProyectoCreateView(RecomendacionProyectoCreateUpdateBase, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una RecomendacionProyecto'''
    permission_required = 'eia_app.add_recomendacionproyecto'


class RecomendacionProyectoUpdateView(RecomendacionProyectoCreateUpdateBase, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una RecomendacionProyecto'''
    permission_required = 'eia_app.change_recomendacionproyecto'

class RecomendacionProyectoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DescripcionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/detail.html'
    permission_required = 'eia_app.view_recomendacionproyecto'

class RecomendacionProyectoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una RecomendacionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-recomendaciones-proyecto')
    permission_required = 'eia_app.delete_recomendacionproyecto'

class RecomendacionProyectoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Listar las RecomendacionProyecto'''
    model = RecomendacionProyecto
    template_name = 'eia_app/recomendaciones_proyecto/list.html'
    permission_required = 'eia_app.view_recomendacionproyecto'


def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)



class ConclusionesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    'Lista de las conclusiones de todos los proyectos'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/list.html'
    permission_required = 'eia_app.view_conclusionproyecto'

class ConclusionAddOrEditBase(LoginRequiredMixin, PermissionRequiredMixin):
    ''' Clase base para la edicion y creacion de conclusiones '''
    model = ConclusionProyecto
    form_class = ConclusionProyectoCreateForm
    template_name = 'eia_app/conclusiones/form.html'
    success_url = reverse_lazy('consultor-crud:lista-conclusiones')


class ConclusionesCreateView(ConclusionAddOrEditBase, CreateView):
    'Crear una conclusión para un proyecto'
    permission_required = 'eia_app.add_conclusionproyecto'
    def form_valid(self, form):
        """
        Sobreescribe la funcion de form_valid
        para poder incluir el proyecto seleccionado
        por el usuario para editar
        """
        usuario_loggeado = self.request.user
        pk_proyecto_editable = usuario_loggeado.proyecto_seleccionado
        proyecto_editable = DatosProyecto.objects.get(pk=pk_proyecto_editable)
        contenido = form.cleaned_data['conclusiones']
        ConclusionProyecto.objects.create(proyecto=proyecto_editable, conclusiones=contenido)
        return redirect(self.success_url)

class ConclusionUpdateView(ConclusionAddOrEditBase, UpdateView):
    'Actualizar datos de una conclusión'
    permission_required = 'eia_app.change_conclusionproyecto'

class ConclusionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    'Eliminar una conclusión de un proyecto'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-conclusiones')
    permission_required = 'eia_app.delete_conclusionproyecto'

class ConclusionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    'Detalles acerca de una conclusión de un proyecto'
    model = ConclusionProyecto
    template_name = 'eia_app/conclusiones/detail.html'
    permission_required = 'eia_app.view_conclusionproyecto'

class MedioList(LoginRequiredMixin, PermissionRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/medios_index.html'
    permission_required = 'eia_app.view_medio'


class MedioCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = Medio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')
    permission_required = 'eia_app.add_medio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar detalles de un medio ambiental"
        return context


class MedioDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un Medio'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/detail.html'
    permission_required = 'eia_app.view_medio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioDetail, self).get_context_data(**kwargs)
        caracteristicas = CaracteristicaMedio.objects.filter(
            medio=self.kwargs['pk'])
        context["caracteristicas"] = caracteristicas
        return context


class MedioUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Medio'''
    model = Medio
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')
    fields = '__all__'
    permission_required = 'eia_app.change_medio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar medio"
        return context


class MedioDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Medio'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')
    permission_required = 'eia_app.delete_medio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioDelete, self).get_context_data(**kwargs)
        context["medio"] = True
        return context


class CaracteristicaMedioDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView): # pylint: disable=too-many-ancestors
    '''Ver caracteristicas de un medio fisico'''
    model = CaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/subcategorias_detail.html'
    permission_required = 'eia_app.view_caracteristicamedio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            CaracteristicaMedioDetail,
            self).get_context_data(**kwargs)
        subcaracteristicas = SubaracteristicaMedio.objects.filter(
            caracteristica=self.kwargs['pk'])
        context["subcaracteristicas"] = subcaracteristicas
        return context


class CaracteristicaMedioUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/create_form.html'
    fields = ['caracteristica', 'descripcion']
    permission_required = 'eia_app.change_caracteristicamedio'

    def get_success_url(self):
        caracteristica = CaracteristicaMedio.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-medio',
                            kwargs={'pk': caracteristica.medio.pk})
    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CaracteristicaMedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar característica de un medio"
        return context


class CaracteristicaMedioDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/delete.html'
    permission_required = 'eia_app.delete_caracteristicamedio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            CaracteristicaMedioDelete,
            self).get_context_data(**kwargs)
        context["caracteristica"] = True
        return context

    def get_success_url(self):
        caracteristica = CaracteristicaMedio.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-medio',
                            kwargs={'pk': caracteristica.medio.pk})


class CaracteristicaMedioCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = CaracteristicaMedio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'
    permission_required = 'eia_app.add_caracteristicamedio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            CaracteristicaMedioCreate,
            self).get_context_data(**kwargs)
        medio = Medio.objects.get(pk=self.kwargs['pk'])
        context["nombre"] = "Agregar características del proyecto " + \
        str(medio.proyecto) + " del medio " + \
        str(medio.tipo)
        context["medio"] = medio.pk
        return context

    def get_success_url(self):
        return reverse_lazy('consultor-crud:detalles-medio',
                            kwargs={'pk': self.kwargs['pk']})


class SubaracteristicaMedioCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = SubaracteristicaMedio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'
    permission_required = 'eia_app.add_subaracteristicamedio'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            SubaracteristicaMedioCreate,
            self).get_context_data(**kwargs)
        caracteristica = CaracteristicaMedio.objects.get(pk=self.kwargs['pk'])
        context["nombre"] = "Agregar sub-característica de la característica " + \
        str(caracteristica.caracteristica) + " del medio " + \
        str(caracteristica.medio.tipo) + " del proyecto " + \
        str(caracteristica.medio.proyecto)
        context["caracteristica"] = caracteristica.pk
        return context

    def get_success_url(self):
        return reverse_lazy('consultor-crud:detalles-caracteristica',
                            kwargs={'pk': self.kwargs['pk']})

class SubaracteristicaMedioUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una SubaracteristicaMedio'''
    model = SubaracteristicaMedio
    template_name = 'eia_app/create_form.html'
    fields = ['nombre_sub', 'atributo', 'comentario']
    permission_required = 'eia_app.change_subaracteristicamedio'

    def get_success_url(self):
        subcaracteristica = SubaracteristicaMedio.objects.get(
            pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-caracteristica',
                            kwargs={'pk': subcaracteristica.caracteristica.pk})

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SubaracteristicaMedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar subcaracterística de un medio"
        return context


class SubaracteristicaMedioDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una SubaracteristicaMedio'''
    model = SubaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/delete.html'
    permission_required = 'eia_app.delete_subaracteristicamedio'

    def get_success_url(self):
        subcaracteristica = SubaracteristicaMedio.objects.get(
            pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-caracteristica',
                            kwargs={'pk': subcaracteristica.caracteristica.pk})

class CostoHumanoList(LoginRequiredMixin, PermissionRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    #context_object_name = 'CostoHumano_list'
    template_name = 'eia_app/Costos/list.html'
    permission_required = 'eia_app.view_costohumano'

    def get_context_data(self, **kwargs): # pylint: disable=arguments-differ
        context = super(CostoHumanoList, self).get_context_data(**kwargs) # pylint: disable=arguments-differ
        context.update({
            'CostoMateriales': CostoMateriales.objects.order_by('proyecto'),
            'pasajes': CostoHumano.objects.filter(tipo=3),
            'servicios': CostoHumano.objects.filter(tipo=2),
            'humanos': CostoHumano.objects.filter(tipo=1),
            'recursos': CostoMateriales.objects.filter(tipo=4),
            'oficina': CostoMateriales.objects.filter(tipo=5),
            'insumos': CostoMateriales.objects.filter(tipo=6),
        })
        if self.kwargs.get('success') is not None:
            context["success"] = self.kwargs.get('success')
        return context

class CostoHumanoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success', kwargs={'success': 'botonHumano'})
    permission_required = 'eia_app.add_costohumano'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de talento humano"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=1)[0]
        return super().form_valid(form)


class CostoHumanoServiciosCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success', kwargs={'success': 'botonServicio'})
    permission_required = 'eia_app.add_costohumano'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoServiciosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de servicios profesionales y técnicos"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=2)[0]
        return super().form_valid(form)

class CostoHumanoPasajeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success',
                               kwargs={'success': 'botonPasaje'})
    permission_required = 'eia_app.add_costohumano'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoPasajeCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costos de pasajes y hospedaje"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=3)[0]
        return super().form_valid(form)

class CostoMaterialRecursosCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success', kwargs={'success': 'botonRecursos'})
    permission_required = 'eia_app.add_costomateriales'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterialRecursosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de recursos materiales"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=4)[0]
        return super().form_valid(form)

class CostoMaterialOficinaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success', kwargs={'success': 'botonOficina'})
    permission_required = 'eia_app.add_costomateriales'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterialOficinaCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de materiales de oficina"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=5)[0]
        return super().form_valid(form)

class CostoMaterialInsumosCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos-success', kwargs={'success': 'botonInsumos'})
    permission_required = 'eia_app.add_costomateriales'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterialInsumosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de insumos"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=6)[0]
        return super().form_valid(form)

class CostoHumanoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar un CostoHumano'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')
    permission_required = 'eia_app.change_costohumano'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar costo humano"
        return context


class CostoHumanoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CostoHumano'''
    model = CostoHumano
    template_name = 'eia_app/Costos/delete.html'
    success_url = reverse_lazy('consultor-crud:costos')
    permission_required = 'eia_app.delete_costohumano'

class CostoMaterialesUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar un CostoMateriales'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')
    permission_required = 'eia_app.change_costomateriales'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterialesUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar costo de materiales"
        return context


class CostoMaterialesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CostoMateriales'''
    model = CostoMateriales
    template_name = 'eia_app/Costos/delete.html'
    success_url = reverse_lazy('consultor-crud:costos')
    permission_required = 'eia_app.delete_costomateriales'
