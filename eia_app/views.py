'''Views del crud del consultor'''

from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    CaracteristicaMedio, Medio, SubaracteristicaMedio, CostoHumano, CostoMateriales, TipoCosto
)
from .forms import (
    OrganizacionCreateForm, SolicitanteCreateForm,
    ResponsableCreateForm, DatosDocumentoCreateForm, DescripcionProyectoCreateForm,
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
        context["nombre"] = "Agregar organización"
        return context


class OrganizacionUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(OrganizacionUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar organización"
        return context

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
    fields = '__all__'
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar datos de un proyecto"
        return context


class DatosProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar datos del proyecto"
        return context


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
        context["nombre"] = "Agregar responsable"
        return context


class ResponsableUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Responsable'''
    model = Responsable
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(ResponsableUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar responsable"
        return context


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
        context["nombre"] = "Agregar solicitante"
        return context


class SolicitanteUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SolicitanteUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar solicitante"
        return context


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
        context["nombre"] = "Agregar datos de un documento"
        return context


class DatosDocumentoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosDocumentoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar datos de un documento"
        return context

class DatosDocumentoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')


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
        context = super(
            DescripcionProyectoCreate,
            self).get_context_data(**kwargs)
        context["nombre"] = "Agregar detalles de un documento"
        return context


class DescripcionProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            DescripcionProyectoUpdate,
            self).get_context_data(**kwargs)
        context["nombre"] = "Editar detalles de un documento"
        return context


class DescripcionProyectoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')


def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)


class MedioList(ListView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/medios_index.html'


class MedioCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = Medio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar detalles de un medio ambiental"
        return context


class MedioDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un Medio'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/detail.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioDetail, self).get_context_data(**kwargs)
        caracteristicas = CaracteristicaMedio.objects.filter(
            medio=self.kwargs['pk'])
        context["caracteristicas"] = caracteristicas
        return context


class MedioUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Medio'''
    model = Medio
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')
    fields = '__all__'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar medio"
        return context


class MedioDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Medio'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioDelete, self).get_context_data(**kwargs)
        context["medio"] = True
        return context


class CaracteristicaMedioDetail(DetailView): # pylint: disable=too-many-ancestors
    '''Ver caracteristicas de un medio fisico'''
    model = CaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/subcategorias_detail.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(
            CaracteristicaMedioDetail,
            self).get_context_data(**kwargs)
        subcaracteristicas = SubaracteristicaMedio.objects.filter(
            caracteristica=self.kwargs['pk'])
        context["subcaracteristicas"] = subcaracteristicas
        return context


class CaracteristicaMedioUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/create_form.html'
    fields = ['caracteristica', 'descripcion']

    def get_success_url(self):
        caracteristica = CaracteristicaMedio.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-medio',
                            kwargs={'pk': caracteristica.medio.pk})
    
    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CaracteristicaMedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar característica de un medio"
        return context


class CaracteristicaMedioDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/delete.html'

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


class CaracteristicaMedioCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = CaracteristicaMedio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'

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


class SubaracteristicaMedioCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = SubaracteristicaMedio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'

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

class SubaracteristicaMedioUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una SubaracteristicaMedio'''
    model = SubaracteristicaMedio
    template_name = 'eia_app/create_form.html'
    fields = ['nombre_sub', 'atributo', 'comentario']

    def get_success_url(self):
        subcaracteristica = SubaracteristicaMedio.objects.get(
            pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-caracteristica',
                            kwargs={'pk': subcaracteristica.caracteristica.pk})
    
    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SubaracteristicaMedioUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar subcaracterística de un medio"
        return context


class SubaracteristicaMedioDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una SubaracteristicaMedio'''
    model = SubaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/delete.html'

    def get_success_url(self):
        subcaracteristica = SubaracteristicaMedio.objects.get(
            pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-caracteristica',
                            kwargs={'pk': subcaracteristica.caracteristica.pk})

class CostoHumanoList(ListView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    #context_object_name = 'CostoHumano_list'
    template_name = 'eia_app/Costos/list.html'

    def get_context_data(self, **kwargs): # pylint: disable=too-many-ancestors
        context = super(CostoHumanoList, self).get_context_data(**kwargs)
        context.update({
            'CostoMateriales': CostoMateriales.objects.order_by('proyecto'),
            'pasajes': CostoHumano.objects.filter(tipo=3),
            'servicios': CostoHumano.objects.filter(tipo=2),
            'humanos': CostoHumano.objects.filter(tipo=1),
            'recursos': CostoMateriales.objects.filter(tipo=4),
            'oficina': CostoMateriales.objects.filter(tipo=5),
            'insumos': CostoMateriales.objects.filter(tipo=6),
            
            

            
        })
        return context

class CostoHumanoCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de talento humano"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=1)[0]
        return super().form_valid(form)


class CostoHumano_ServiciosCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumano_ServiciosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de servicios profesionales y técnicos"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=2)[0]
        return super().form_valid(form)

class CostoHumano_PasajeCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumano_PasajeCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costos de pasajes y hospedaje"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=3)[0]
        return super().form_valid(form)

class CostoMaterial_RecursosCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterial_RecursosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de recursos materiales"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=4)[0]
        return super().form_valid(form)

class CostoMaterial_OficinaCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterial_OficinaCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de materiales de oficina"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=5)[0]
        return super().form_valid(form)

class CostoMaterial_InsumosCreate(CreateView): # pylint: disable=too-many-ancestors
    ''' Index de los distintos medios'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterial_InsumosCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Agregar costo de insumos"
        return context

    def form_valid(self, form):
        form.instance.tipo = TipoCosto.objects.filter(id=6)[0]
        return super().form_valid(form)

class CostoHumanoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar un CostoHumano'''
    model = CostoHumano
    fields = ['proyecto', 'actividad', 'cantidad', 'tiempo', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoHumanoUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar costo humano"
        return context


class CostoHumanoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CostoHumano'''
    model = CostoHumano
    template_name = 'eia_app/Costos/delete.html'
    success_url = reverse_lazy('consultor-crud:costos')

class CostoMaterialesUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar un CostoMateriales'''
    model = CostoMateriales
    fields = ['proyecto', 'material', 'cantidad', 'costo_unidad', 'monto']
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:costos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CostoMaterialesUpdate, self).get_context_data(**kwargs)
        context["nombre"] = "Editar costo de materiales"
        return context


class CostoMaterialesDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CostoMateriales'''
    model = CostoMateriales
    template_name = 'eia_app/Costos/delete.html'
    success_url = reverse_lazy('consultor-crud:costos')