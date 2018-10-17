from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 


# Formularios 
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario 

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario 
    list_display = ['correo']

admin.site.register(Usuario, CustomUserAdmin)
