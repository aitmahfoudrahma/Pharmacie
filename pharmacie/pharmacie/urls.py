
from django.urls import path
from pharmacieapp.views import medicament_list,fournisseur_list, create_medicament
urlpatterns = [
    path('', medicament_list, name='medicament_list'),  # Rediriger l'URL racine vers la liste des médicaments
    path('medicaments/', medicament_list, name='medicament_list'),
    path('fournisseurs/', fournisseur_list, name='fournisseur_list'),
    path('medicaments/create/', create_medicament, name='create_medicament'),
]
