'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (articles/views.py)
FECHA: 29/10/2024
VERSION: 1.0
'''

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import CommentForm
from .models import Comment

# Create your views here.

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment']  # Solo permitimos editar el texto del comentario
    template_name = 'comment_edit.html'
    success_url = reverse_lazy('article_list')  # Redirigir después de la edición

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Permitir solo si es el autor

class CommentGet(LoginRequiredMixin, DetailView):
    model = Article
    template_name= "article_detail.html"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentPost (SingleObjectMixin, FormView):
    
    model = Article
    form_class = CommentForm
    template_name= "article_detail.html"
    
    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment= form.save(commit=False)
        comment.article = self.get_object()
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})



class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin,View):
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def get(self,request,*args, **kwargs):
        view = CommentGet.as_view()
        return view(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        view = CommentPost.as_view()
        return view(request,*args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body",)
    template_name = "article_detail.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")
    template= "article_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)