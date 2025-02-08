'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: NEWSPAPER (accounts/urls.py)
FECHA: 29/09/2024
VERSION: 1.0
'''

from django.urls import path
from .views import SignUpView, ProfileDetailView, FollowUserView, ProfilePictureUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # Coloca la ruta para actualizar la foto antes de la ruta dinámica
    path('profile/update_picture/', ProfilePictureUpdateView.as_view(), name='update_profile_picture'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<str:username>/follow/', FollowUserView.as_view(), name='follow_user'),
]