from django.db import models

"""
Supposez que les modèles Taxi et Client existent déjà dans une autre application.
Importez-les ici pour les relations ForeignKey.
"""
from app_membre.models import Insertion_membre
from app_accueil.models import Insertion_voiture


class Reservation(models.Model):
    client = models.CharField(max_length=100, blank=True, null=True)
    taxi = models.ForeignKey(Insertion_voiture, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations")
    destination = models.CharField(max_length=100)
    compagnie_vol = models.CharField(max_length=100)
    date_reservation = models.DateTimeField(auto_now_add=True)
    date_depart = models.DateTimeField(blank=True, null=True)
    ville_depart = models.CharField(max_length=100,blank=True, null=True)
    nombre_personnes = models.PositiveIntegerField()
    bagages = models.BooleanField(default=False)
    commentaire = models.TextField(blank=True, null=True)
    numero_reservation = models.CharField(max_length=20, unique=True,null=True, blank=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email_client = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Reservation de {self.client} avec {self.compagnie_vol} pour {self.destination} le {self.date_depart.strftime('%Y-%m-%d %H:%M:%S') if self.date_depart else 'date non définie'}"
