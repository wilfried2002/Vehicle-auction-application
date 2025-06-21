from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('buyer', 'Acheteur'),
        ('seller', 'Vendeur'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')  # Valeur par défaut facultative

    def __str__(self):
        return f"Profil de {self.user.username}"
# Create your models here.
