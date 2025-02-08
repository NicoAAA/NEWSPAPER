'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/views.py)
FECHA: 29/09/2024
VERSION: 1.0
'''
# Importamos la función render de Django.
from django.shortcuts import render

# Importamos la clase CreateView de Django.
from django.views.generic import CreateView

# Importamos la función reverse_lazy de Django.
from django.urls import reverse_lazy

# Importamos el formulario CustomUserCreationForm.
from .forms import CustomUserCreationForm

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from articles.models import Article



from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

# Create your views here.

class SignUpView(CreateView):
    '''
    Clase SignUpView que hereda de CreateView. Esta clase se encarga de definir
    la vista para el formulario de registro de un usuario.
    '''
    
    # Definimos el formulario CustomUserCreationForm.
    form_class = CustomUserCreationForm
    
    # Definimos la plantilla de la vista.
    template_name = 'registration/signup.html'
    
    # Definimos la URL a la que se redirige después de registrar un usuario.
    success_url = reverse_lazy('login')



class ProfileDetailView(DetailView):
    '''
    Vista para mostrar el perfil de un usuario específico.
    '''
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        '''
        Obtiene el perfil del usuario basado en el nombre de usuario en la URL.
        '''
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        '''
        Agrega los posts del usuario al contexto.
        '''
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(author=self.get_object().user)
        return context

@method_decorator(login_required, name='dispatch')
class FollowUserView(View):
    '''
    Vista para seguir y dejar de seguir a un usuario.
    '''
    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user_to_follow)

        if request.user in profile.followers.all():
            profile.followers.remove(request.user)  # Si ya sigue, dejar de seguir
        else:
            profile.followers.add(request.user)  # Si no sigue, seguir

        return redirect('profile', username=username)


class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update_profile_picture.html'

    def get_object(self, queryset=None):
        # Solo permitimos actualizar el perfil del usuario autenticado.
        return self.request.user.profile

    def get_success_url(self):
        # Redirige al perfil del usuario después de guardar los cambios.
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})