
from django.urls import path
from pharmacieapp.views import *
urlpatterns = [
    path('', homepage, name='homepage'),
    path('medicaments/', medicament_list, name='medicament_list'),
    path('fournisseurs/', fournisseur_list, name='fournisseur_list'),
    path('clients/', clients_list, name='clients_list'),
    path('assurances/', assurances_list, name='assurances_list'),
    path('ventes/', ventes_list, name='ventes_list'),
    path('commandes/', commandes_list, name='commandes_list'),

    path('medicaments/create/', create_medicament, name='create_medicament'),

]
