''' views.py '''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario

# Create your views here.
class NewUser(View):
    ''' Classes based view encargada del registro de nuevo usuario'''
    form_class = CustomUserCreationForm
    def get(self, request, *args, **kwargs):
        ''' Metodo get de la clase'''
        form = self.form_class()
        return render(request, 'new_user.html', {'form': form})
    def post(self, request, *args, **kwargs):
        ''' Metodo post de la clase'''
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            form.save()
            return redirect('edit_user', user.pk)

def details_user(request, usuario):
    ''' Funcion encargada de la vista de perfil de usuario'''
    user = Usuario.objects.get(pk=usuario)
    return render(request, 'details_user.html', {'user': user})

def edit_user(request, usuario):
    ''' Funcion encargada de la vista de edición de usuario'''
    user = Usuario.objects.get(pk=usuario)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            form.save()
            messages.info(request, 'Datos actualizados exitosamente')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})
