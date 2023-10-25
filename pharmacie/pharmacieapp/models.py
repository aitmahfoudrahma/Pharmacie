from django.db import models
from django.db import models

# Modèle pour la table "Medicament"
class Medicament(models.Model):
    Nom_medic = models.CharField(max_length=100)
    Lot_medic = models.CharField(max_length=20)
    DCI = models.CharField(max_length=100)
    Dosage_medic = models.IntegerField()
    Prix_médic = models.DecimalField(max_digits=5, decimal_places=2)
    Prix_achat = models.DecimalField(max_digits=5, decimal_places=2)
    Forme_medic = models.CharField(max_length=20)
    Prémption_medic = models.DateField()
    Quantite_medic = models.IntegerField()

    def __str__(self):
        return self.Nom_medic

# Modèle pour la table "Fournisseur"
class Fournisseur(models.Model):
    Nom_fournisseur = models.CharField(max_length=100)
    Adresse_fournisseur = models.CharField(max_length=200)
    Tel_fournisseur = models.IntegerField()
    Mail_fournisseur = models.EmailField()

    def __str__(self):
        return self.Nom_fournisseur

# Modèle pour la table "Client"
class Client(models.Model):
    Nom_client = models.CharField(max_length=100)
    Prenom_client = models.CharField(max_length=100)
    Age_Client = models.IntegerField()
    Num_sec_social_client = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"{self.Prenom_client} {self.Nom_client}"
class Commande(models.Model):
    Id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    ID_medic = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    Date_commande = models.DateField()
    Quantite_commande = models.IntegerField()

    def __str__(self):
        return f"Commande {self.id}"

# Modèle pour la table "Vente"
class Vente(models.Model):
    ID_medic = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    ID_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date_vente = models.DateField()
    Quantite_vendue = models.IntegerField()

    def __str__(self):
        return f"Vente {self.id}"

# Modèle pour la table "Assurance"
class Assurance(models.Model):
    Num_sec_social_client = models.CharField(max_length=13)
    Type_assurance = models.IntegerField()  # Assurez-vous d'utiliser le bon type de champ pour le type d'assurance.

    def __str__(self):
        return f"Assurance pour {self.Num_sec_social_client}"