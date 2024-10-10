'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/views.py)
FECHA: 29/09/2024
VERSION: 1.0
'''
# Importamos la función render de Django.
from django.shortcuts import render

# Importamos la clase CreateView de Django.
from django.views.generic import CreateView

# Importamos la función reverse_lazy de Django.
from django.urls import reverse_lazy

# Importamos el formulario CustomUserCreationForm.
from .forms import CustomUserCreationForm



# Create your views here.

class SignUpView(CreateView):
    '''
    Clase SignUpView que hereda de CreateView. Esta clase se encarga de definir
    la vista para el formulario de registro de un usuario.
    '''
    
    # Definimos el formulario CustomUserCreationForm.
    form_class = CustomUserCreationForm
    
    # Definimos la plantilla de la vista.
    template_name = 'registration/signup.html'
    
    # Definimos la URL a la que se redirige después de registrar un usuario.
    success_url = reverse_lazy('login')