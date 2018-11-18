'''Views del crud del consultor'''

from django.shortcuts import render, redirect
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView,
                                  FormView)
from django.urls import reverse_lazy
from django.db.models import Q
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento
)
from .forms import (
    OrganizacionCreateForm, SolicitanteCreateForm,
    ResponsableCreateForm, DatosDocumentoCreateForm, DatosProyectoCreateForm,
    MarcoForm
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

class MarcoListView(ListView):
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
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

    def get(self, request, *args, **kwargs):
        self.template_name = self.template_name.format(tipo=kwargs.get('tipo'))
        return super().get(request, *args, **kwargs)

class MarcoCreateView(FormView):
    """ Vista que permite crear un marco metodologico a un proyecto """
    form_class = MarcoForm
    template_name = 'eia_app/marco_form.html'
    success_url = reverse_lazy('consultor-crud:lista-marcos')
    def get_context_data(self):
        context = super().get_context_data()
        context['edicion'] = self.kwargs.get('pk', None) != None
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk', None)
        if pk is None:
            return kwargs
        proyecto = DatosProyecto.objects.get(pk=pk)
        tipo = self.kwargs.get('tipo')
        if tipo == 'metodologico':
            contenido = proyecto.marco_metodologico
        elif tipo == 'teorico':
            contenido = proyecto.marco_teorico
        else:
            contenido = proyecto.marco_juridico
        kwargs['initial']['contenido'] = contenido
        kwargs['initial']['proyecto'] = pk
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


class MarcoDetailView(DetailView):
    template_name = "eia_app/marco_{tipo}/detail.html"
    model = DatosProyecto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = self.kwargs.get('tipo')
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = self.template_name.format(tipo=kwargs.get('tipo'))
        return super().get(request, *args, **kwargs)

def delete_marco_view(request, tipo, pk):
    proyecto = DatosProyecto.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'eia_app/marco_{tipo}/delete.html'.format(tipo=tipo),
                      {'object':proyecto})

    if tipo == 'metodologico':
        proyecto.marco_metodologico = None
    elif tipo == 'juridico':
        proyecto.marco_juridico = None
    else:
        proyecto.marco_teorico = None
    proyecto.save()
    return redirect(reverse_lazy('consultor-crud:lista-marcos', kwargs={'tipo': tipo}))

def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)
