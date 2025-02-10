'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/forms.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

# Importamos el formulario UserCreationForm y UserChangeForm de Django.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Importamos el modelo CustomUser.
from .models import CustomUser
from django import forms
from .models import Profile

# Definimos la clase CustomUserCreationForm que hereda de UserCreationForm.
class CustomUserCreationForm(UserCreationForm):
    '''
    Clase CustomUserCreationForm que hereda de UserCreationForm. Esta clase se
    encarga de definir el formulario para la creación de un usuario.
    '''
    
    class Meta(UserCreationForm.Meta):
        '''
        Clase Meta que hereda de UserCreationForm.Meta. Esta clase se encarga
        de definir el modelo y los campos del formulario.
        '''
        
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )

# Definimos la clase CustomUserChangeForm que hereda de UserChangeForm.
class CustomUserChangeForm(UserChangeForm):
    '''
    Clase CustomUserChangeForm que hereda de UserChangeForm. Esta clase se
    encarga de definir el formulario para la actualización de un usuario.
    '''
    
    class Meta(UserChangeForm.Meta):
        '''
        Clase Meta que hereda de UserChangeForm.Meta. Esta clase se encarga
        de definir el modelo y los campos del formulario.
        '''
        
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        labels = {
            'profile_picture': 'Foto de perfil',  # Cambia el texto de la etiqueta a español.
        }
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mi-clase-personalizada',  # Aquí puedes agregar clases CSS.
                # Puedes agregar otros atributos si lo deseas.
            }),
        }