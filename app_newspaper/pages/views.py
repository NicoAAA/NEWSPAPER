'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (pages/views.py)
FECHA: 29/09/2024
VERSION: 1.0
'''


# Impotacion de la funcion render para renderizar la pagina principal
from django.shortcuts import render

# Importacion de la clase TemplateView para renderizar la pagina principal
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    '''
    Esta clase se encarga de renderizar la pagina principal
    y cargar el template home.html en la carpeta templates.
    '''
    template_name= 'home.html'