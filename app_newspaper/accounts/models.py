'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/models.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

# Importamos el modelo AbstractUser de Django.
from django.contrib.auth.models import AbstractUser

# Importamos el modelo models de Django.
from django.db import models

# Importamos el modelo User de Django.
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    '''
    Clase CustomUser que hereda de AbstractUser. Esta clase se encarga de
    definir los campos de la tabla de la base de datos que se va a crear
    para el modelo CustomUser.
    '''
    
    # Definimos el camopo age como un campo entero positivo.
    age = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def total_followers(self):
        return self.followers.count()