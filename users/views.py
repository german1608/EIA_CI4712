''' views.py '''
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario
# Create your views here.

def new_user(request):
    ''' texto '''
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            form.save()
            return redirect('edit_user',user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'new_user.html', {'form': form})

def details_user(request, pk):
    user = Usuario.objects.get(pk=pk)
    return render(request,'details_user.html', {'user': user})

def edit_user(request, pk):
    user = Usuario.objects.get(pk=pk)

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

