from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import Vehicle
from django.contrib.auth.decorators import login_required

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
    if vehicule_id:
        vehicule = Vehicle.objects.get(id=vehicule_id, vendeur=request.user)
    else:
        vehicule = None

    if request.method == 'POST':
        marque = request.POST.get('marque')
        modele = request.POST.get('modele')
        annee = request.POST.get('annee')
        prix = request.POST.get('prix')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if vehicule:
            vehicule.marque = marque
            vehicule.modele = modele
            vehicule.annee = annee
            vehicule.prix = prix
            vehicule.description = description
            if image:
                vehicule.image = image
            vehicule.save()
        else:
            Vehicle.objects.create(
                vendeur=request.user,
                marque=marque,
                modele=modele,
                annee=annee,
                prix=prix,
                description=description,
                image=image
            )

        return redirect('vendeur_dashboard')

    return render(request, 'vendeur/ajouter_modifier.html', {
        'vehicule': vehicule,
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

