''' views.py '''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario
# Create your views here.

class NewUser(CreateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la creacion de un nuevo usuario'''
    model = Usuario
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('new_user')

    def form_valid(self, form):
        form.instance.username = form.cleaned_data['email']
        return super().form_valid(form)

class UpdateUser(UpdateView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la edicion de un usuario'''
    model = Usuario
    form_class = CustomUserChangeForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('new_user')

class DeleteUser(DeleteView): # pylint: disable=too-many-ancestors
    ''' Class based view encargada de la eliminacion de un usuario'''
    model = Usuario
    success_url = reverse_lazy('new_user')
