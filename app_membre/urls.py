from django.urls import path
from.views import*
from django.contrib.auth import views

urlpatterns = [
    path("page_connexion/",page_connexion,name="page_connexion"),
    path("souscrire_membre/",page_souscription,name="page_souscription"),
    path("souscrire_membre",souscrire_membre,name="souscrire_membre"),
    path("connexion_membre",connexion_membre,name="connexion_membre"),
    path("deconnexion_membre",deconnexion_membre,name="deconnexion_membre"),
    # REINITIALISATION MOT DE PASSE
    path("reset_password/",views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path("reset_password",reset_password,name="reset_password"),
    path("reset_password/<str:token>",page_reset_password,name=""),
<<<<<<< HEAD
    path("reset_password/<str:token>",page_reset_password,name=""),
    path("profil/",page_profil,name="profil"),
    path("profil",modifier_profil,name="modifier_profil"),
    path("supprimer_profil",supprimer_profil,name="supprimer_profil"),
=======

>>>>>>> 7e02915e25e3b5cd32e9302e0022bd14962040b8
]
