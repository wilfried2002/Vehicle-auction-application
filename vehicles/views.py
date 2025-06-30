from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import Vehicle
from django.db.models import DecimalField #type: ignore
from decimal import Decimal, InvalidOperation
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required
# def ajouter_vehicule(request):
#     if request.method == 'POST':
#         form = VehicleForm(request.POST, request.FILES)
#         if form.is_valid():
#             vehicule = form.save(commit=False)
#             vehicule.vendeur = request.user
#             vehicule.save()
#             return redirect('mes_vehicules')
#     else:
#         form = VehicleForm()
#     return render(request, 'vehicules/ajouter_vehicule.html', {'form': form})



@login_required
def ajouter_modifier_vehicule(request, vehicule_id=None):
    vehicule = None

    if vehicule_id:
        vehicule = get_object_or_404(Vehicle, id=vehicule_id, vendeur=request.user) # type: ignore

    if request.method == 'POST':
        marque = request.POST.get('marque')
        modele = request.POST.get('modele')
        annee = request.POST.get('annee')
        description = request.POST.get('description')
        prix_str = request.POST.get('prix', '0').replace(',', '').replace(' ', '').strip()
        image = request.FILES.get('image')

        try:
            prix_decimal = Decimal(prix_str)
        except (InvalidOperation, ValueError):
            messages.error(request, "Prix invalide, valeur mise à 0.")
            prix_decimal = Decimal(0)

        if vehicule:
            vehicule.marque = marque
            vehicule.modele = modele
            vehicule.annee = annee
            vehicule.description = description
            vehicule.prix = prix_decimal
            if image:
                vehicule.image = image
            vehicule.save()
            messages.success(request, "Véhicule modifié avec succès.")
            return redirect('mes_vehicules')
        else:
            Vehicle.objects.create(
                vendeur=request.user,
                marque=marque,
                modele=modele,
                annee=annee,
                description=description,
                prix=prix_decimal,
                image=image
            )
            messages.success(request, "Véhicule ajouté avec succès.")

        return redirect('vendeur_dashboard')

    return render(request, 'vendeur/ajouter_modifier.html', {
        'vehicule': vehicule
    })


@login_required
def mes_vehicules(request):
    vehicules = Vehicle.objects.filter(vendeur=request.user)
    return render(request, 'vehicules/mes_vehicules.html', {'vehicules': vehicules})

@login_required
def vendeur_dashboard(request):
    vehicules = Vehicle.objects.filter(vendeur=request.user).order_by('-date_ajout')
    return render(request, 'dashboard/seller_dashboard.html', {'vehicules': vehicules})

@login_required
def marquer_comme_vendu(request, vehicule_id):
    vehicule = Vehicle.objects.get(id=vehicule_id, vendeur=request.user)
    vehicule.est_vendu = True
    vehicule.save()
    return redirect('vendeur_dashboard')

