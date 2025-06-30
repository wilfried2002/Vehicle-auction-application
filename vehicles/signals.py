from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Vehicle

@receiver(user_logged_in)
def assign_vehicules_to_user(sender, user, request, **kwargs):
    # ATTENTION : cette logique est à adapter à ton besoin métier réel
    Vehicle.objects.filter(vendeur__isnull=True).update(vendeur=user)
