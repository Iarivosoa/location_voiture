from .views import *
from django.urls import path
urlpatterns = [
    path('reservation/<int:id>',res, name='reservation'),
    path('reservation/', reservation, name='reserver'),
    # path('envoyer_whatsapp/', envoyer_whatsapp, name='envoyer_whatsapp'),
    path("serviceRapide",envoyer_whatsapp, name="envoyer_whatsapp"),
    # reservation rapide
    path("reservation",reservation,name="reservation"),
    # page de historique des réservations
    path("historique", historique, name="historique"),
    path("supprimer_reservation/<int:reservation_id>/", supprimer_reservation, name="supprimer_reservation"),
    path("contact_admin/", contact_admin, name="contact_admin"),
]
