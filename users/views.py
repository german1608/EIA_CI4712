''' views.py '''
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.

def new_user(request):
    ''' texto '''
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            form.save()
            return redirect('new_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'new_user.html', {'form': form})
