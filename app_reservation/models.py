from django.db import models

"""
Supposez que les modèles Taxi et Client existent déjà dans une autre application.
Importez-les ici pour les relations ForeignKey.
"""
from app_membre.models import Insertion_membre
from app_accueil.models import Insertion_voiture


class Reservation(models.Model):
    client = models.ForeignKey(Insertion_membre, on_delete=models.CASCADE, related_name="reservations")
    taxi = models.ForeignKey(Insertion_voiture, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations")
    destination = models.CharField(max_length=100)
    compagnie_vol = models.CharField(max_length=100)
    date_reservation = models.DateTimeField(auto_now_add=True)
    Heure_arriver = models.DateTimeField()
    nombre_personnes = models.PositiveIntegerField()
    bagages = models.BooleanField(default=False)
    commentaire = models.TextField(blank=True, null=True)
    numero_reservation = models.CharField(max_length=20, unique=True,null=True, blank=True)

    def __str__(self):
        return f"Reservation de {self.client} avec {self.compagnie_vol} le {self.Heure_arriver.strftime('%d/%m/%Y %H:%M')}"
