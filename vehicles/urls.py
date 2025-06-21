from . import views
from django.urls import path


urlpatterns = [
    path('dashboard/', views.vendeur_dashboard, name='vendeur_dashboard'),
    path('ajouter/', views.ajouter_modifier_vehicule, name='ajouter_vehicule'),
    path('mes-vehicules/', views.mes_vehicules, name='mes_vehicules'),
    path('modifier/<int:vehicule_id>/', views.ajouter_modifier_vehicule, name='modifier_vehicule'),
    path('marquer-vendu/<int:vehicule_id>/', views.marquer_comme_vendu, name='marquer_vendu'),
    

]
