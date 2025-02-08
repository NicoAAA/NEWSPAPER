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
from .models import Comment, Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'image')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'new-comment custom-form-control mt-2', 'placeholder': 'Escribe un comentario...'})
    )
    
    