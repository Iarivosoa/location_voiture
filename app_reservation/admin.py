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
        'date_depart',
        'ville_depart',
        'nombre_personnes',
        'bagages',
        'date_reservation',
        'numero_reservation',
        'commentaire',
    )
    list_filter = ('date_reservation', 'compagnie_vol', 'destination', 'bagages','date_depart','ville_depart')
    search_fields = ('client__nom', 'client__prenom', 'compagnie_vol', 'taxi__numero','numero_reservation')
