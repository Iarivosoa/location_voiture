from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from .views import*

urlpatterns = [
    path("",affiche_index,name="accueil"),
    path("detail/<int:id>",detail,name="detail"),
    path("chargement",chargement,name="chargement"),
    path("service",service,name="service"),
    path("offre",offre,name="offre"),
    path("contacte_admin",contacte_admin,name="contacte_admin"),
    # affiche appropos.html
    path("appropos",appropos,name="appropos"),
    path('i18n/', include('django.conf.urls.i18n')),

    # URL CHANGEMENT DE LANGUE
]
