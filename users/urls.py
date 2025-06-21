from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('seller_dashboard_view/', views.seller_dashboard_view, name='seller_dashboard_view'),
    path('buyer_dashboard_view/', views.buyer_dashboard_view, name='buyer_dashboard_view'),
    path('register/', views.register, name='register'),
    # path('redirect/', views.redirection_tableau_de_bord, name='redirect_tableau_de_bord'),
   # path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    


]
