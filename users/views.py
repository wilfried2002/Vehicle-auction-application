from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse



@login_required(login_url='login')
def seller_dashboard_view(request):
    if request.user.profile.role == 'seller':
        return render(request, 'dashboard/seller_dashboard.html')
    else:
        return render(request, 'unauthorized.html')  # ou tu peux rediriger ailleurs

#dashboard pour les vendeurs
# @login_required
# def seller_dashboard_view(request):
#     return render(request, 'dashboard/seller_dashboard.html')

@login_required(login_url='login')
def buyer_dashboard_view(request):
    if request.user.profile.role == 'buyer':
        return render(request, 'dashboard/buyer_dashboard.html')
    else:
        return render(request, 'unauthorized.html') 
    

def home_view(request):
    return render(request, 'home_view.html')


#vue pour l'inscription des utilisateurs

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")

        # Vérification des mots de passe
        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, "users/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return render(request, "users/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, "users/register.html")

        # Création de l'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password1)

        # Mise à jour du rôle du profil automatiquement créé via signal
        user.profile.role = role
        user.profile.save()

        # Connexion automatique
        login(request, user)
        messages.success(request, "Inscription réussie !")

        # Redirection selon rôle
        if role == "buyer":
            return redirect("buyer_dashboard_view")
        else:
            return redirect("seller_dashboard_view")

    return render(request, "users/register.html")




#vue pour gerer les acces non autorisés
def unauthorized(request):
    return render(request, 'unauthorized.html')

#login view pour authentifier les utilisateurs

# def custom_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             # Redirection selon le rôle
#             if user.profile.role == 'seller':
#                 return redirect('dashboard/seller_dashboard.html')
#             else:
#                 return redirect('dashboard/buyer_dashboard.html')
#         else:
#             messages.error(request, 'Nom d’utilisateur ou mot de passe invalide.')

#     return render(request, 'users/login.html')




def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                profile = user.profile  # ✅ Vérification que le profil existe
            except Profile.DoesNotExist:
                messages.error(request, "Ce compte n’a pas encore de profil associé.")
                return redirect('login')

            login(request, user)

            # ✅ Redirection selon le rôle
            if profile.role == 'seller':
                return redirect('seller_dashboard_view')  # Nom de l'URL, pas le chemin
            else:
                return redirect('buyer_dashboard_view')
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe invalide.')

    return render(request, 'users/login.html')


# Vue pour la déconnexion
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('login')  # Assure-toi que 'login' est bien défini dans tes urls

# Vue pour tester l'envoi d'un e-mail

# def test_email(request):
#     send_mail(
#         'Test Django',
#         'Ceci est un e-mail de test.',
#         'ngankouwilfried8@gmail.com',
#         ['briceduplex7@gmail.com'],  # à toi-même pour tester
#         fail_silently=False,
#     )
#     return HttpResponse("Email envoyé")
