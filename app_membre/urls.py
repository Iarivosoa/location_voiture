from django.urls import path
from.views import*

urlpatterns = [
    path("page_connexion",page_connexion,name="page_connexion"),
    path("page_souscription",page_souscription,name="page_souscription"),
    path("souscrire_membre",souscrire_membre,name="souscrire_membre"),
    path("connexion_membre",connexion_membre,name="connexion_membre"),
    path("deconnexion_membre",deconnexion_membre,name="deconnexion_membre")
]
