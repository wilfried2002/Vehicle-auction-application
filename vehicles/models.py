from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"