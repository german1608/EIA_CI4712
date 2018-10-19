from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import CustomUserCreationForm
# Create your views here.

def index(request):
    return HttpResponse("Hello World. You're at the users index.")

def new_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('new_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'new_user.html', {'form': form})