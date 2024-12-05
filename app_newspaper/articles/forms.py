'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (articles/forms.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment","author")
    