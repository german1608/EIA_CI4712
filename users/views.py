''' views.py '''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario
# Create your views here.

class NewUser(LoginRequiredMixin, PermissionRequiredMixin, CreateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la creacion de un nuevo usuario'''
    model = Usuario
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('new_user')
    permission_required = 'users.add_usuario'

class UpdateUser(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la edicion de un usuario'''
    model = Usuario
    form_class = CustomUserChangeForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('new_user')
    permission_required = 'users.change_usuario'
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['rol'] = self.object.groups.all().first().pk
        return kwargs

class DeleteUser(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la eliminacion de un usuario'''
    model = Usuario
    success_url = reverse_lazy('new_user')
    permission_required = 'users.delete_usuario'

class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de listar todos los usuarios de la tabla Usuario'''
    model = Usuario
    permission_required = 'users.view_usuario'
