from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['marque', 'modele', 'annee', 'prix', 'description', 'image']