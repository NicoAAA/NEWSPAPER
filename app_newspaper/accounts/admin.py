'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/admin.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

# Importamos el modelo CustomUser.
from django.contrib import admin

# Importamos el modelo CustomUser.
from django.contrib.auth.admin import UserAdmin

# Importamos el modelo CustomUser.
from .models import CustomUser

# Importamos el formulario CustomUserCreationForm y CustomUserChangeForm.
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

class CustomUserAdmin(UserAdmin):
    '''
    Clase CustomUserAdmin que hereda de UserAdmin. Esta clase se encarga de
    definir el modelo y los campos que se van a mostrar en el panel de
    administración de Django.
    '''
    
    
    # Definimos el formulario CustomUserCreationForm.
    add_form = CustomUserCreationForm
    
    # Definimos el formulario CustomUserChangeForm.
    form = CustomUserChangeForm
    
    # Definimos el modelo CustomUser.
    model = CustomUser
    
    # Definimos los campos que se van a mostrar en el panel de administración.
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
        ]
    
    # Definimos los campos que se van a mostrar en el panel de administración.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    
    # Definimos los campos que se van a mostrar en el panel de administración.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)