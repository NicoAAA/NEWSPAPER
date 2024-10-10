'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (articles/admin.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

from django.contrib import admin
from .models import Article

# Register your models here.

admin.site.register(Article)

