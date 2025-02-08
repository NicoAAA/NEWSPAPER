from django.db.models.signals import post_save
from django.contrib.auth import get_user_model  # Importa get_user_model
from django.dispatch import receiver
from .models import Profile

User = get_user_model()  # Esto obtiene el modelo correcto definido en AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Asegúrate de que el profile existe antes de intentar guardarlo.
    if hasattr(instance, 'profile'):
        instance.profile.save()
