from .views import*
from django.urls import path

urlpatterns = [
    path('page_vacance',page_vacance,name="page_vacance"),
    path('voyage/',voyage,name="voyage"),
    # page tarif
    path("tarif",tarif,name="tarif"),
    # page reserveRapide
    path("rapide",rapide,name="rapide"),
    # afficher tous les voitures pour une résevartion rapide
    path("tousVoiture",tousVoiture,name="tousVoiture"),
    # pour service rapide.html
    path("serviceRapide/",serviceRapide,name="serviceRapide"),
    # OFFRE DISPO
    path("offre_site",offre,name="offre_site"),
    # detail pour les offres park
    path("service_detail/<int:id>",service_detail,name="service_detail")
    
]
