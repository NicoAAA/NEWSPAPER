'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (articles/urls.py)
FECHA: 29/10/2024
VERSION: 1.0
'''
from django.urls import path
from .views import (
      ArticleListView,
      ArticleDetailView,
      ArticleUpdateView,
      ArticleDeleteView,
      ArticleCreateView,
      CommentUpdateView,
      ArticleListCommentView,
      article_search,
)


# Definimos la lista de URLs de la aplicación articles.
urlpatterns = [
    path ("<int:pk>/" , ArticleDetailView.as_view(), name="article_detail"
          ),
    path ("<int:pk>/edit/" , ArticleUpdateView.as_view(), name="article_edit"
          ),
    path ("<int:pk>/delete/" , ArticleDeleteView.as_view(), name="article_delete"
          ),
    path ("new/" , ArticleCreateView.as_view(), 
    name='article_new'
          ),
    path('', ArticleListView.as_view(), 
    name='article_list'
         ),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('article-comment/', ArticleListCommentView.as_view(), name='article_comment'),
    path('search/', article_search, name='article_search'),
    
]