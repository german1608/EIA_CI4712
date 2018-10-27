from django import forms
from .models import *

class OrganizacionCreateForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = '__all__'