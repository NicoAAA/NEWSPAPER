'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (pages/urls.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

# Importacion de la funcion path para definir las rutas de la aplicacion
from django.urls import path

# Importacion de la clase HomePageView para renderizar la pagina principal
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # Definicion de la ruta de la pagina principal
]
