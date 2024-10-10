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

# Create your models here.

class CustomUser(AbstractUser):
    '''
    Clase CustomUser que hereda de AbstractUser. Esta clase se encarga de
    definir los campos de la tabla de la base de datos que se va a crear
    para el modelo CustomUser.
    '''
    
    # Definimos el camopo age como un campo entero positivo.
    age = models.PositiveIntegerField(null=True, blank=True)