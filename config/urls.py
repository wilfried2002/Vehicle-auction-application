"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from users import views 
from vehicles import views as vehicle_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('vehicule/', include('vehicles.urls')),
    path('dashboard/seller_dashboard_view/', views.seller_dashboard_view, name='seller_dashboard_view'),
    path('dashboard/buyer_dashboard_view/', views.buyer_dashboard_view, name='buyer_dashboard_view'),
    # path('redirect/', views.redirection_tableau_de_bord, name='redirect_tableau_de_bord'),
    # path('register/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # ✅ Route par défaut (accueil)
    path('', views.home_view, name='home'),


    # Étape 1 : formulaire pour entrer l’e-mail
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_form.html'), name='password_reset'),

    # Étape 2 : message indiquant que le mail a été envoyé
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),

    # Étape 3 : formulaire pour entrer un nouveau mot de passe via le lien du mail
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # Étape 4 : confirmation de la réinitialisation du mot de passe
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),

        # path('test-email/', views.test_email),
    # Route pour tester l'envoi d'un e-mail

    #Gestion des véhicules

    
    path('dashboard/', vehicle_views.vendeur_dashboard, name='vendeur_dashboard'),
   
    path('ajouter/', vehicle_views.ajouter_modifier_vehicule, name='ajouter_vehicule'),
    path('mes-vehicules/', vehicle_views.mes_vehicules, name='mes_vehicules'),
    path('modifier/<int:vehicule_id>/', vehicle_views.ajouter_modifier_vehicule, name='modifier_vehicule'),
    path('marquer-vendu/<int:vehicule_id>/', vehicle_views.marquer_comme_vendu, name='marquer_vendu'),

]
