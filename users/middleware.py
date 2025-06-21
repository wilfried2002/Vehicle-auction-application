# from django.shortcuts import redirect
# from django.contrib import messages

# class AdminAccessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         path = request.path

#         # Si l'utilisateur essaie d'accéder à /admin (ou sous-chemins)
#         if path.startswith('/admin/'):
#             # Laisse Django afficher la page de connexion normalement
#             if not request.user.is_authenticated:
#                 return self.get_response(request)

#             # Si connecté mais non staff, on redirige vers l’accueil
#             if not request.user.is_staff:
#                 messages.error(request, "Accès refusé : vous n'avez pas les droits pour accéder à l'administration.")
#                 return redirect('/')

#         return self.get_response(request)
