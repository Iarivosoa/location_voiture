from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'taxi',
        'destination',
        'compagnie_vol',
        'date_reservation',
        'Heure_arriver',
        'nombre_personnes',
        'bagages',
        'date_reservation',
        'numero_reservation',
        'commentaire',
    )
    list_filter = ('date_reservation', 'compagnie_vol', 'destination', 'bagages','Heure_arriver')
    search_fields = ('client__nom', 'client__prenom', 'compagnie_vol', 'taxi__numero','numero_reservation')
