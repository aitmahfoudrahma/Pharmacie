from django.shortcuts import render, redirect
from .models import *

def homepage(request):
    return  render(request, 'homepage.html')
def medicament_list(request):
    medicaments = Medicament.objects.all()
    return render(request, 'medicament_list.html', {'medicaments': medicaments})

def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseur_list.html', {'fournisseurs': fournisseurs})

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})
def assurances_list(request):
    assurances = Assurance.objects.all()
    return render(request, 'assurances_list.html', {'assurances': assurances})
def ventes_list(request):
    ventes = Vente.objects.all()
    return render(request, 'ventes_list.html', {'ventes': ventes})
def commandes_list(request):
    commandes = Commande.objects.all()
    return render(request, 'commandes_list.html', {'commandes': commandes})

medicament = Medicament(
    Nom_medic='Aspirin',
    Lot_medic='123ABC',
    DCI='Acetylsalicylic acid',
    Dosage_medic=100,
    Prix_médic=5.99,
    Prix_achat=3.99,
    Forme_medic='Comprimé',
    Prémption_medic='2024-12-31',
    Quantite_medic=500
)
#medicament.save()

from .forms import MedicamentForm

def create_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicament_list')
    else:
        form = MedicamentForm()
    return render(request, 'medicament_form.html', {'form': form})

