from django.shortcuts import render, redirect
from .models import Medicament, Fournisseur

def medicament_list(request):
    medicaments = Medicament.objects.all()
    return render(request, 'medicament_list.html', {'medicaments': medicaments})

def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseur_list.html', {'fournisseurs': fournisseurs})


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
medicament.save()

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
