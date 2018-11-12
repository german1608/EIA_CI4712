''' views.py '''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario
# Create your views here.

class NewUser(CreateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la creacion de un nuevo usuario'''
    model = Usuario
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('new_user')

class UpdateUser(UpdateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la edicion de un usuario'''
    model = Usuario
    form_class = CustomUserChangeForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('new_user')
    def get_form_kwargs(self, *a, **kw):
        kwargs = super().get_form_kwargs(*a, **kw)
        kwargs['initial']['rol'] = self.object.groups.all().first().pk
        return kwargs

class DeleteUser(DeleteView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la eliminacion de un usuario'''
    model = Usuario
    success_url = reverse_lazy('new_user')

class UserList(ListView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de listar todos los usuarios de la tabla Usuario'''
    model = Usuario
