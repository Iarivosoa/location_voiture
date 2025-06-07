from django.urls import path
from .views import*

urlpatterns = [
    path("",affiche_index,name="accueil"),
    path("detail/<int:id>",detail,name="detail"),
    path("chargement",chargement,name="chargement"),
    path("service",service,name="service"),
    path("offre",offre,name="offre"),
]
